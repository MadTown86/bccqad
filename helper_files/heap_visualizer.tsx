import React, { useState, useEffect } from 'react';

const HeapVisualizer = () => {
  const [heap, setHeap] = useState([42, 35, 28, 15, 20, 10, 8, 5, 12]);
  const [animatingNodes, setAnimatingNodes] = useState(new Set());
  const [comparingNodes, setComparingNodes] = useState(new Set());
  const [newValue, setNewValue] = useState('');
  const [isMaxHeap, setIsMaxHeap] = useState(true);
  const [animationSpeed, setAnimationSpeed] = useState(1000);

  const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

  const compare = (a, b) => {
    return isMaxHeap ? a > b : a < b;
  };

  const getParentIndex = (i) => Math.floor((i - 1) / 2);
  const getLeftChildIndex = (i) => 2 * i + 1;
  const getRightChildIndex = (i) => 2 * i + 2;

  const bubbleUp = async (startIndex, newHeap) => {
    let currentIndex = startIndex;
    
    while (currentIndex > 0) {
      const parentIndex = getParentIndex(currentIndex);
      
      setComparingNodes(new Set([currentIndex, parentIndex]));
      await sleep(animationSpeed);
      
      if (compare(newHeap[currentIndex], newHeap[parentIndex])) {
        // Swap needed
        setAnimatingNodes(new Set([currentIndex, parentIndex]));
        await sleep(animationSpeed / 2);
        
        [newHeap[currentIndex], newHeap[parentIndex]] = [newHeap[parentIndex], newHeap[currentIndex]];
        setHeap([...newHeap]);
        
        await sleep(animationSpeed / 2);
        setAnimatingNodes(new Set());
        
        currentIndex = parentIndex;
      } else {
        break;
      }
      
      setComparingNodes(new Set());
    }
    
    setComparingNodes(new Set());
    setAnimatingNodes(new Set());
  };

  const bubbleDown = async (startIndex, newHeap) => {
    let currentIndex = startIndex;
    
    while (true) {
      let targetIndex = currentIndex;
      const leftChild = getLeftChildIndex(currentIndex);
      const rightChild = getRightChildIndex(currentIndex);
      
      const nodesToCompare = new Set([currentIndex]);
      
      if (leftChild < newHeap.length) {
        nodesToCompare.add(leftChild);
        if (compare(newHeap[leftChild], newHeap[targetIndex])) {
          targetIndex = leftChild;
        }
      }
      
      if (rightChild < newHeap.length) {
        nodesToCompare.add(rightChild);
        if (compare(newHeap[rightChild], newHeap[targetIndex])) {
          targetIndex = rightChild;
        }
      }
      
      setComparingNodes(nodesToCompare);
      await sleep(animationSpeed);
      
      if (targetIndex !== currentIndex) {
        // Swap needed
        setAnimatingNodes(new Set([currentIndex, targetIndex]));
        await sleep(animationSpeed / 2);
        
        [newHeap[currentIndex], newHeap[targetIndex]] = [newHeap[targetIndex], newHeap[currentIndex]];
        setHeap([...newHeap]);
        
        await sleep(animationSpeed / 2);
        setAnimatingNodes(new Set());
        
        currentIndex = targetIndex;
      } else {
        break;
      }
      
      setComparingNodes(new Set());
    }
    
    setComparingNodes(new Set());
    setAnimatingNodes(new Set());
  };

  const insertValue = async () => {
    if (!newValue || isNaN(parseInt(newValue))) return;
    
    const value = parseInt(newValue);
    const newHeap = [...heap, value];
    setHeap(newHeap);
    setNewValue('');
    
    await sleep(500);
    await bubbleUp(newHeap.length - 1, newHeap);
  };

  const extractRoot = async () => {
    if (heap.length === 0) return;
    
    const newHeap = [...heap];
    
    if (newHeap.length === 1) {
      setHeap([]);
      return;
    }
    
    // Move last element to root
    newHeap[0] = newHeap[newHeap.length - 1];
    newHeap.pop();
    setHeap([...newHeap]);
    
    await sleep(500);
    await bubbleDown(0, newHeap);
  };

  const resetHeap = () => {
    setHeap([42, 35, 28, 15, 20, 10, 8, 5, 12]);
    setAnimatingNodes(new Set());
    setComparingNodes(new Set());
  };

  const toggleHeapType = () => {
    setIsMaxHeap(!isMaxHeap);
    // Convert current heap to opposite type
    const newHeap = [...heap].sort((a, b) => !isMaxHeap ? b - a : a - b);
    setHeap(newHeap);
  };

  const getNodePosition = (index, totalNodes) => {
    if (totalNodes === 0) return { x: 0, y: 0 };
    
    const level = Math.floor(Math.log2(index + 1));
    const positionInLevel = index - (Math.pow(2, level) - 1);
    const nodesInLevel = Math.pow(2, level);
    
    const levelWidth = Math.min(nodesInLevel * 80, 600);
    const startX = (600 - levelWidth) / 2;
    
    const x = startX + (positionInLevel * (levelWidth / nodesInLevel)) + (levelWidth / nodesInLevel) / 2;
    const y = 60 + level * 80;
    
    return { x, y };
  };

  const renderConnections = () => {
    const connections: React.JSX.Element[] = [];
    
    for (let i = 1; i < heap.length; i++) {
      const parentIndex = getParentIndex(i);
      const parentPos = getNodePosition(parentIndex, heap.length);
      const childPos = getNodePosition(i, heap.length);
      
      connections.push(
        <line
          key={`connection-${i}`}
          x1={parentPos.x}
          y1={parentPos.y}
          x2={childPos.x}
          y2={childPos.y}
          stroke="#cbd5e1"
          strokeWidth="2"
        />
      );
    }
    
    return connections;
  };

  const renderNodes = () => {
    return heap.map((value, index) => {
      const pos = getNodePosition(index, heap.length);
      const isAnimating = animatingNodes.has(index);
      const isComparing = comparingNodes.has(index);
      
      return (
        <g key={`node-${index}`}>
          <circle
            cx={pos.x}
            cy={pos.y}
            r="25"
            fill={isAnimating ? "#ef4444" : isComparing ? "#f59e0b" : "#3b82f6"}
            stroke={isAnimating || isComparing ? "#1f2937" : "#1e40af"}
            strokeWidth="2"
            className={isAnimating ? "animate-pulse" : ""}
          />
          <text
            x={pos.x}
            y={pos.y + 5}
            textAnchor="middle"
            fill="white"
            fontSize="14"
            fontWeight="bold"
          >
            {value}
          </text>
        </g>
      );
    });
  };

  return (
    <div className="p-6 max-w-4xl mx-auto bg-gray-50 rounded-lg">
      <h1 className="text-3xl font-bold text-center mb-6 text-gray-800">
        Interactive Heap Visualizer
      </h1>
      
      <div className="mb-6 flex flex-wrap gap-4 justify-center items-center">
        <div className="flex items-center gap-2">
          <input
            type="number"
            value={newValue}
            onChange={(e) => setNewValue(e.target.value)}
            placeholder="Enter value"
            className="px-3 py-2 border rounded-md w-32"
          />
          <button
            onClick={insertValue}
            disabled={animatingNodes.size > 0 || comparingNodes.size > 0}
            className="px-4 py-2 bg-green-500 text-white rounded-md hover:bg-green-600 disabled:opacity-50"
          >
            Insert & Bubble Up
          </button>
        </div>
        
        <button
          onClick={extractRoot}
          disabled={animatingNodes.size > 0 || comparingNodes.size > 0 || heap.length === 0}
          className="px-4 py-2 bg-red-500 text-white rounded-md hover:bg-red-600 disabled:opacity-50"
        >
          Extract Root & Bubble Down
        </button>
        
        <button
          onClick={toggleHeapType}
          disabled={animatingNodes.size > 0 || comparingNodes.size > 0}
          className="px-4 py-2 bg-purple-500 text-white rounded-md hover:bg-purple-600 disabled:opacity-50"
        >
          Switch to {isMaxHeap ? 'Min' : 'Max'} Heap
        </button>
        
        <button
          onClick={resetHeap}
          disabled={animatingNodes.size > 0 || comparingNodes.size > 0}
          className="px-4 py-2 bg-gray-500 text-white rounded-md hover:bg-gray-600 disabled:opacity-50"
        >
          Reset
        </button>
      </div>
      
      <div className="mb-4 flex justify-center items-center gap-4">
        <label className="flex items-center gap-2">
          <span className="text-sm font-medium">Animation Speed:</span>
          <input
            type="range"
            min="200"
            max="2000"
            step="200"
            value={animationSpeed}
            onChange={(e) => setAnimationSpeed(parseInt(e.target.value))}
            className="w-32"
          />
          <span className="text-sm text-gray-600">{animationSpeed}ms</span>
        </label>
      </div>
      
      <div className="text-center mb-4">
        <div className="inline-flex items-center gap-4 text-sm">
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 bg-blue-500 rounded-full"></div>
            <span>Normal Node</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 bg-amber-500 rounded-full"></div>
            <span>Comparing</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 bg-red-500 rounded-full"></div>
            <span>Swapping</span>
          </div>
        </div>
      </div>
      
      <div className="bg-white rounded-lg p-4 shadow-md">
        <div className="text-center mb-4">
          <h2 className="text-xl font-semibold text-gray-700">
            {isMaxHeap ? 'Max Heap' : 'Min Heap'} - Root: {heap.length > 0 ? heap[0] : 'Empty'}
          </h2>
        </div>
        
        <svg width="600" height="400" className="mx-auto border rounded">
          {renderConnections()}
          {renderNodes()}
        </svg>
      </div>
      
      <div className="mt-6 bg-white rounded-lg p-4 shadow-md">
        <h3 className="text-lg font-semibold mb-3">How it works:</h3>
        <div className="grid md:grid-cols-2 gap-4 text-sm">
          <div>
            <h4 className="font-medium text-blue-600 mb-2">Bubble Up (Insert):</h4>
            <p>When inserting a new value, it's added at the end of the heap. Then it "bubbles up" by comparing with its parent and swapping if needed, until the heap property is restored.</p>
          </div>
          <div>
            <h4 className="font-medium text-red-600 mb-2">Bubble Down (Extract):</h4>
            <p>When extracting the root, the last element replaces it. This element then "bubbles down" by comparing with its children and swapping with the appropriate child until the heap property is restored.</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HeapVisualizer;