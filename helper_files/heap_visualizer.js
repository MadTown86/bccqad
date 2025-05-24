"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g = Object.create((typeof Iterator === "function" ? Iterator : Object).prototype);
    return g.next = verb(0), g["throw"] = verb(1), g["return"] = verb(2), typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (g && (g = 0, op[0] && (_ = 0)), _) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
Object.defineProperty(exports, "__esModule", { value: true });
var react_1 = require("react");
var HeapVisualizer = function () {
    var _a = (0, react_1.useState)([42, 35, 28, 15, 20, 10, 8, 5, 12]), heap = _a[0], setHeap = _a[1];
    var _b = (0, react_1.useState)(new Set()), animatingNodes = _b[0], setAnimatingNodes = _b[1];
    var _c = (0, react_1.useState)(new Set()), comparingNodes = _c[0], setComparingNodes = _c[1];
    var _d = (0, react_1.useState)(''), newValue = _d[0], setNewValue = _d[1];
    var _e = (0, react_1.useState)(true), isMaxHeap = _e[0], setIsMaxHeap = _e[1];
    var _f = (0, react_1.useState)(1000), animationSpeed = _f[0], setAnimationSpeed = _f[1];
    var sleep = function (ms) { return new Promise(function (resolve) { return setTimeout(resolve, ms); }); };
    var compare = function (a, b) {
        return isMaxHeap ? a > b : a < b;
    };
    var getParentIndex = function (i) { return Math.floor((i - 1) / 2); };
    var getLeftChildIndex = function (i) { return 2 * i + 1; };
    var getRightChildIndex = function (i) { return 2 * i + 2; };
    var bubbleUp = function (startIndex, newHeap) { return __awaiter(void 0, void 0, void 0, function () {
        var currentIndex, parentIndex;
        var _a;
        return __generator(this, function (_b) {
            switch (_b.label) {
                case 0:
                    currentIndex = startIndex;
                    _b.label = 1;
                case 1:
                    if (!(currentIndex > 0)) return [3 /*break*/, 7];
                    parentIndex = getParentIndex(currentIndex);
                    setComparingNodes(new Set([currentIndex, parentIndex]));
                    return [4 /*yield*/, sleep(animationSpeed)];
                case 2:
                    _b.sent();
                    if (!compare(newHeap[currentIndex], newHeap[parentIndex])) return [3 /*break*/, 5];
                    // Swap needed
                    setAnimatingNodes(new Set([currentIndex, parentIndex]));
                    return [4 /*yield*/, sleep(animationSpeed / 2)];
                case 3:
                    _b.sent();
                    _a = [newHeap[parentIndex], newHeap[currentIndex]], newHeap[currentIndex] = _a[0], newHeap[parentIndex] = _a[1];
                    setHeap(__spreadArray([], newHeap, true));
                    return [4 /*yield*/, sleep(animationSpeed / 2)];
                case 4:
                    _b.sent();
                    setAnimatingNodes(new Set());
                    currentIndex = parentIndex;
                    return [3 /*break*/, 6];
                case 5: return [3 /*break*/, 7];
                case 6:
                    setComparingNodes(new Set());
                    return [3 /*break*/, 1];
                case 7:
                    setComparingNodes(new Set());
                    setAnimatingNodes(new Set());
                    return [2 /*return*/];
            }
        });
    }); };
    var bubbleDown = function (startIndex, newHeap) { return __awaiter(void 0, void 0, void 0, function () {
        var currentIndex, targetIndex, leftChild, rightChild, nodesToCompare;
        var _a;
        return __generator(this, function (_b) {
            switch (_b.label) {
                case 0:
                    currentIndex = startIndex;
                    _b.label = 1;
                case 1:
                    if (!true) return [3 /*break*/, 7];
                    targetIndex = currentIndex;
                    leftChild = getLeftChildIndex(currentIndex);
                    rightChild = getRightChildIndex(currentIndex);
                    nodesToCompare = new Set([currentIndex]);
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
                    return [4 /*yield*/, sleep(animationSpeed)];
                case 2:
                    _b.sent();
                    if (!(targetIndex !== currentIndex)) return [3 /*break*/, 5];
                    // Swap needed
                    setAnimatingNodes(new Set([currentIndex, targetIndex]));
                    return [4 /*yield*/, sleep(animationSpeed / 2)];
                case 3:
                    _b.sent();
                    _a = [newHeap[targetIndex], newHeap[currentIndex]], newHeap[currentIndex] = _a[0], newHeap[targetIndex] = _a[1];
                    setHeap(__spreadArray([], newHeap, true));
                    return [4 /*yield*/, sleep(animationSpeed / 2)];
                case 4:
                    _b.sent();
                    setAnimatingNodes(new Set());
                    currentIndex = targetIndex;
                    return [3 /*break*/, 6];
                case 5: return [3 /*break*/, 7];
                case 6:
                    setComparingNodes(new Set());
                    return [3 /*break*/, 1];
                case 7:
                    setComparingNodes(new Set());
                    setAnimatingNodes(new Set());
                    return [2 /*return*/];
            }
        });
    }); };
    var insertValue = function () { return __awaiter(void 0, void 0, void 0, function () {
        var value, newHeap;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    if (!newValue || isNaN(parseInt(newValue)))
                        return [2 /*return*/];
                    value = parseInt(newValue);
                    newHeap = __spreadArray(__spreadArray([], heap, true), [value], false);
                    setHeap(newHeap);
                    setNewValue('');
                    return [4 /*yield*/, sleep(500)];
                case 1:
                    _a.sent();
                    return [4 /*yield*/, bubbleUp(newHeap.length - 1, newHeap)];
                case 2:
                    _a.sent();
                    return [2 /*return*/];
            }
        });
    }); };
    var extractRoot = function () { return __awaiter(void 0, void 0, void 0, function () {
        var newHeap;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    if (heap.length === 0)
                        return [2 /*return*/];
                    newHeap = __spreadArray([], heap, true);
                    if (newHeap.length === 1) {
                        setHeap([]);
                        return [2 /*return*/];
                    }
                    // Move last element to root
                    newHeap[0] = newHeap[newHeap.length - 1];
                    newHeap.pop();
                    setHeap(__spreadArray([], newHeap, true));
                    return [4 /*yield*/, sleep(500)];
                case 1:
                    _a.sent();
                    return [4 /*yield*/, bubbleDown(0, newHeap)];
                case 2:
                    _a.sent();
                    return [2 /*return*/];
            }
        });
    }); };
    var resetHeap = function () {
        setHeap([42, 35, 28, 15, 20, 10, 8, 5, 12]);
        setAnimatingNodes(new Set());
        setComparingNodes(new Set());
    };
    var toggleHeapType = function () {
        setIsMaxHeap(!isMaxHeap);
        // Convert current heap to opposite type
        var newHeap = __spreadArray([], heap, true).sort(function (a, b) { return !isMaxHeap ? b - a : a - b; });
        setHeap(newHeap);
    };
    var getNodePosition = function (index, totalNodes) {
        if (totalNodes === 0)
            return { x: 0, y: 0 };
        var level = Math.floor(Math.log2(index + 1));
        var positionInLevel = index - (Math.pow(2, level) - 1);
        var nodesInLevel = Math.pow(2, level);
        var levelWidth = Math.min(nodesInLevel * 80, 600);
        var startX = (600 - levelWidth) / 2;
        var x = startX + (positionInLevel * (levelWidth / nodesInLevel)) + (levelWidth / nodesInLevel) / 2;
        var y = 60 + level * 80;
        return { x: x, y: y };
    };
    var renderConnections = function () {
        var connections = [];
        for (var i = 1; i < heap.length; i++) {
            var parentIndex = getParentIndex(i);
            var parentPos = getNodePosition(parentIndex, heap.length);
            var childPos = getNodePosition(i, heap.length);
            connections.push(<line key={"connection-".concat(i)} x1={parentPos.x} y1={parentPos.y} x2={childPos.x} y2={childPos.y} stroke="#cbd5e1" strokeWidth="2"/>);
        }
        return connections;
    };
    var renderNodes = function () {
        return heap.map(function (value, index) {
            var pos = getNodePosition(index, heap.length);
            var isAnimating = animatingNodes.has(index);
            var isComparing = comparingNodes.has(index);
            return (<g key={"node-".concat(index)}>
          <circle cx={pos.x} cy={pos.y} r="25" fill={isAnimating ? "#ef4444" : isComparing ? "#f59e0b" : "#3b82f6"} stroke={isAnimating || isComparing ? "#1f2937" : "#1e40af"} strokeWidth="2" className={isAnimating ? "animate-pulse" : ""}/>
          <text x={pos.x} y={pos.y + 5} textAnchor="middle" fill="white" fontSize="14" fontWeight="bold">
            {value}
          </text>
        </g>);
        });
    };
    return (<div className="p-6 max-w-4xl mx-auto bg-gray-50 rounded-lg">
      <h1 className="text-3xl font-bold text-center mb-6 text-gray-800">
        Interactive Heap Visualizer
      </h1>
      
      <div className="mb-6 flex flex-wrap gap-4 justify-center items-center">
        <div className="flex items-center gap-2">
          <input type="number" value={newValue} onChange={function (e) { return setNewValue(e.target.value); }} placeholder="Enter value" className="px-3 py-2 border rounded-md w-32"/>
          <button onClick={insertValue} disabled={animatingNodes.size > 0 || comparingNodes.size > 0} className="px-4 py-2 bg-green-500 text-white rounded-md hover:bg-green-600 disabled:opacity-50">
            Insert & Bubble Up
          </button>
        </div>
        
        <button onClick={extractRoot} disabled={animatingNodes.size > 0 || comparingNodes.size > 0 || heap.length === 0} className="px-4 py-2 bg-red-500 text-white rounded-md hover:bg-red-600 disabled:opacity-50">
          Extract Root & Bubble Down
        </button>
        
        <button onClick={toggleHeapType} disabled={animatingNodes.size > 0 || comparingNodes.size > 0} className="px-4 py-2 bg-purple-500 text-white rounded-md hover:bg-purple-600 disabled:opacity-50">
          Switch to {isMaxHeap ? 'Min' : 'Max'} Heap
        </button>
        
        <button onClick={resetHeap} disabled={animatingNodes.size > 0 || comparingNodes.size > 0} className="px-4 py-2 bg-gray-500 text-white rounded-md hover:bg-gray-600 disabled:opacity-50">
          Reset
        </button>
      </div>
      
      <div className="mb-4 flex justify-center items-center gap-4">
        <label className="flex items-center gap-2">
          <span className="text-sm font-medium">Animation Speed:</span>
          <input type="range" min="200" max="2000" step="200" value={animationSpeed} onChange={function (e) { return setAnimationSpeed(parseInt(e.target.value)); }} className="w-32"/>
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
    </div>);
};
exports.default = HeapVisualizer;
