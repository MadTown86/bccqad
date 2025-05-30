"""
Complete Search Algorithms Implementation in Python
==================================================

This file contains implementations of all major search algorithms
organized by category with examples and test cases.

Author: Generated for educational purposes
"""

import math
import heapq
from collections import deque, defaultdict
from typing import List, Optional, Tuple, Dict, Any
import random


# =============================================================================
# LINEAR SEARCH ALGORITHMS
# =============================================================================

def linear_search(arr: List[Any], target: Any) -> int:
    """
    Linear search through array sequentially.
    Time: O(n), Space: O(1)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def sentinel_linear_search(arr: List[Any], target: Any) -> int:
    """
    Linear search with sentinel to reduce comparisons.
    Time: O(n), Space: O(1)
    """
    if not arr:
        return -1
    
    # Store the last element and replace with target
    last = arr[-1]
    arr[-1] = target
    
    i = 0
    while arr[i] != target:
        i += 1
    
    # Restore the last element
    arr[-1] = last
    
    # Check if target was found or if we reached the sentinel
    if i < len(arr) - 1 or arr[-1] == target:
        return i
    return -1


# =============================================================================
# BINARY SEARCH ALGORITHMS
# =============================================================================

def binary_search_iterative(arr: List[Any], target: Any) -> int:
    """
    Iterative binary search on sorted array.
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_recursive(arr: List[Any], target: Any, left: int = 0, right: int = None) -> int:
    """
    Recursive binary search on sorted array.
    Time: O(log n), Space: O(log n)
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def exponential_search(arr: List[Any], target: Any) -> int:
    """
    Exponential search for unbounded/large arrays.
    Time: O(log n), Space: O(1)
    """
    if not arr:
        return -1
    
    if arr[0] == target:
        return 0
    
    # Find range for binary search
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    
    # Binary search in found range
    return binary_search_iterative(arr[i//2:min(i, len(arr))], target)


def interpolation_search(arr: List[int], target: int) -> int:
    """
    Interpolation search for uniformly distributed sorted data.
    Time: O(log log n) average, O(n) worst, Space: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right and target >= arr[left] and target <= arr[right]:
        # If array has only one element
        if left == right:
            return left if arr[left] == target else -1
        
        # Interpolation formula
        pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    
    return -1


def ternary_search(arr: List[Any], target: Any) -> int:
    """
    Ternary search on sorted array.
    Time: O(log₃ n), Space: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        
        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    
    return -1


# =============================================================================
# JUMP/BLOCK SEARCH ALGORITHMS
# =============================================================================

def jump_search(arr: List[Any], target: Any) -> int:
    """
    Jump search on sorted array.
    Time: O(√n), Space: O(1)
    """
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    
    # Find block where element may be present
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    # Linear search in found block
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    
    if arr[prev] == target:
        return prev
    
    return -1


def fibonacci_search(arr: List[Any], target: Any) -> int:
    """
    Fibonacci search on sorted array.
    Time: O(log n), Space: O(1)
    """
    n = len(arr)
    
    # Initialize fibonacci numbers
    fib_m2 = 0  # (m-2)'th Fibonacci number
    fib_m1 = 1  # (m-1)'th Fibonacci number
    fib_m = fib_m2 + fib_m1  # m'th Fibonacci number
    
    # Find smallest Fibonacci number >= n
    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1
    
    offset = -1
    
    while fib_m > 1:
        # Check if fib_m2 is valid location
        i = min(offset + fib_m2, n - 1)
        
        if arr[i] < target:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        elif arr[i] > target:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
        else:
            return i
    
    # Check last element
    if fib_m1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1
    
    return -1


# =============================================================================
# TREE-BASED SEARCH
# =============================================================================

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class BST:
    """Binary Search Tree implementation."""
    
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        self.root = self._insert_recursive(self.root, val)
    
    def _insert_recursive(self, node, val):
        if not node:
            return TreeNode(val)
        
        if val < node.val:
            node.left = self._insert_recursive(node.left, val)
        else:
            node.right = self._insert_recursive(node.right, val)
        
        return node
    
    def search(self, val) -> bool:
        """Search for value in BST. Time: O(log n) average, O(n) worst"""
        return self._search_recursive(self.root, val)
    
    def _search_recursive(self, node, val):
        if not node:
            return False
        
        if node.val == val:
            return True
        elif val < node.val:
            return self._search_recursive(node.left, val)
        else:
            return self._search_recursive(node.right, val)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_word = False


class Trie:
    """Trie (Prefix Tree) implementation for string search."""
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        """Insert word into trie. Time: O(m) where m is word length"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_word = True
    
    def search(self, word: str) -> bool:
        """Search for complete word. Time: O(m)"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_word
    
    def starts_with(self, prefix: str) -> bool:
        """Check if any word starts with prefix. Time: O(m)"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# =============================================================================
# HASH-BASED SEARCH
# =============================================================================

class HashTable:
    """Simple hash table implementation with chaining."""
    
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        """Insert key-value pair. Time: O(1) average"""
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key, value))
    
    def search(self, key) -> Optional[Any]:
        """Search for key. Time: O(1) average, O(n) worst"""
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        return None


class BloomFilter:
    """Bloom filter for membership testing."""
    
    def __init__(self, size=1000, hash_count=3):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [False] * size
    
    def _hashes(self, item):
        """Generate multiple hash values for an item."""
        hashes = []
        for i in range(self.hash_count):
            hashes.append(hash(str(item) + str(i)) % self.size)
        return hashes
    
    def add(self, item):
        """Add item to bloom filter. Time: O(1)"""
        for h in self._hashes(item):
            self.bit_array[h] = True
    
    def contains(self, item) -> bool:
        """Check if item might be in set. Time: O(1)"""
        for h in self._hashes(item):
            if not self.bit_array[h]:
                return False
        return True


# =============================================================================
# GRAPH SEARCH ALGORITHMS
# =============================================================================

class Graph:
    """Graph implementation for search algorithms."""
    
    def __init__(self):
        self.graph = defaultdict(list)
        self.weights = {}  # For weighted graphs
    
    def add_edge(self, u, v, weight=1):
        self.graph[u].append(v)
        self.weights[(u, v)] = weight
    
    def bfs(self, start, target) -> Optional[List]:
        """Breadth-First Search. Time: O(V + E)"""
        if start == target:
            return [start]
        
        visited = set()
        queue = deque([(start, [start])])
        visited.add(start)
        
        while queue:
            node, path = queue.popleft()
            
            for neighbor in self.graph[node]:
                if neighbor == target:
                    return path + [neighbor]
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        return None
    
    def dfs(self, start, target, visited=None, path=None) -> Optional[List]:
        """Depth-First Search. Time: O(V + E)"""
        if visited is None:
            visited = set()
        if path is None:
            path = []
        
        visited.add(start)
        path = path + [start]
        
        if start == target:
            return path
        
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                result = self.dfs(neighbor, target, visited, path)
                if result:
                    return result
        
        return None
    
    def dijkstra(self, start, target) -> Tuple[Optional[int], Optional[List]]:
        """Dijkstra's shortest path algorithm. Time: O((V + E) log V)"""
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        previous = {}
        
        pq = [(0, start)]
        visited = set()
        
        while pq:
            current_distance, current = heapq.heappop(pq)
            
            if current in visited:
                continue
            
            visited.add(current)
            
            if current == target:
                # Reconstruct path
                path = []
                while current in previous:
                    path.append(current)
                    current = previous[current]
                path.append(start)
                return distances[target], path[::-1]
            
            for neighbor in self.graph[current]:
                weight = self.weights.get((current, neighbor), 1)
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current
                    heapq.heappush(pq, (distance, neighbor))
        
        return None, None


def a_star_search(graph, start, goal, heuristic):
    """
    A* search algorithm with heuristic.
    Time: O(b^d) where b is branching factor, d is depth
    """
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    
    while open_set:
        current = heapq.heappop(open_set)[1]
        
        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + 1  # Assuming unit weight
            
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None


def bidirectional_search(graph, start, goal):
    """
    Bidirectional search from both ends.
    Time: O(b^(d/2)) where b is branching factor, d is depth
    """
    if start == goal:
        return [start]
    
    # Initialize both searches
    visited_start = {start}
    visited_goal = {goal}
    queue_start = deque([(start, [start])])
    queue_goal = deque([(goal, [goal])])
    
    while queue_start or queue_goal:
        # Expand from start
        if queue_start:
            node, path = queue_start.popleft()
            for neighbor in graph[node]:
                if neighbor in visited_goal:
                    # Find the path from goal to neighbor
                    for goal_node, goal_path in queue_goal:
                        if goal_node == neighbor:
                            return path + goal_path[::-1][1:]
                
                if neighbor not in visited_start:
                    visited_start.add(neighbor)
                    queue_start.append((neighbor, path + [neighbor]))
        
        # Expand from goal
        if queue_goal:
            node, path = queue_goal.popleft()
            for neighbor in graph[node]:
                if neighbor in visited_start:
                    # Find the path from start to neighbor
                    for start_node, start_path in queue_start:
                        if start_node == neighbor:
                            return start_path + path[::-1][1:]
                
                if neighbor not in visited_goal:
                    visited_goal.add(neighbor)
                    queue_goal.append((neighbor, path + [neighbor]))
    
    return None


# =============================================================================
# STRING SEARCH ALGORITHMS
# =============================================================================

def naive_string_search(text: str, pattern: str) -> List[int]:
    """
    Naive string matching algorithm.
    Time: O(n*m), Space: O(1)
    """
    positions = []
    n, m = len(text), len(pattern)
    
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            positions.append(i)
    
    return positions


def kmp_search(text: str, pattern: str) -> List[int]:
    """
    Knuth-Morris-Pratt string matching algorithm.
    Time: O(n + m), Space: O(m)
    """
    def compute_failure_function(pattern):
        m = len(pattern)
        failure = [0] * m
        j = 0
        
        for i in range(1, m):
            while j > 0 and pattern[i] != pattern[j]:
                j = failure[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            failure[i] = j
        
        return failure
    
    positions = []
    n, m = len(text), len(pattern)
    
    if m == 0:
        return positions
    
    failure = compute_failure_function(pattern)
    j = 0
    
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = failure[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            positions.append(i - m + 1)
            j = failure[j - 1]
    
    return positions


def boyer_moore_search(text: str, pattern: str) -> List[int]:
    """
    Boyer-Moore string matching algorithm.
    Time: O(n/m) best, O(n*m) worst, Space: O(m + σ)
    """
    def bad_character_table(pattern):
        table = {}
        for i in range(len(pattern)):
            table[pattern[i]] = i
        return table
    
    positions = []
    n, m = len(text), len(pattern)
    
    if m == 0:
        return positions
    
    bad_char = bad_character_table(pattern)
    i = 0
    
    while i <= n - m:
        j = m - 1
        
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        
        if j < 0:
            positions.append(i)
            i += 1
        else:
            # Bad character rule
            bad_char_shift = j - bad_char.get(text[i + j], -1)
            i += max(1, bad_char_shift)
    
    return positions


def rabin_karp_search(text: str, pattern: str, prime=101) -> List[int]:
    """
    Rabin-Karp string matching using rolling hash.
    Time: O(n + m) average, O(n*m) worst, Space: O(1)
    """
    positions = []
    n, m = len(text), len(pattern)
    d = 256  # Number of characters in alphabet
    
    if m == 0:
        return positions
    
    pattern_hash = 0
    text_hash = 0
    h = 1
    
    # Calculate h = pow(d, m-1) % prime
    for i in range(m - 1):
        h = (h * d) % prime
    
    # Calculate initial hash values
    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % prime
        text_hash = (d * text_hash + ord(text[i])) % prime
    
    # Slide pattern over text
    for i in range(n - m + 1):
        # Check if hash values match
        if pattern_hash == text_hash:
            # Check characters one by one
            if text[i:i+m] == pattern:
                positions.append(i)
        
        # Calculate hash for next window
        if i < n - m:
            text_hash = (d * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if text_hash < 0:
                text_hash += prime
    
    return positions


# =============================================================================
# SPECIALIZED SEARCH ALGORITHMS
# =============================================================================

def quickselect(arr: List[int], k: int) -> int:
    """
    QuickSelect algorithm to find kth smallest element.
    Time: O(n) average, O(n²) worst, Space: O(1)
    """
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    def quickselect_helper(arr, low, high, k):
        if low == high:
            return arr[low]
        
        pivot_index = partition(arr, low, high)
        
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return quickselect_helper(arr, low, pivot_index - 1, k)
        else:
            return quickselect_helper(arr, pivot_index + 1, high, k)
    
    if not arr or k < 0 or k >= len(arr):
        return None
    
    return quickselect_helper(arr[:], 0, len(arr) - 1, k)


class BinaryIndexedTree:
    """
    Binary Indexed Tree (Fenwick Tree) for range sum queries.
    Time: O(log n) for query and update, Space: O(n)
    """
    
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
    
    def update(self, i, delta):
        """Add delta to element at index i."""
        while i <= self.size:
            self.tree[i] += delta
            i += i & (-i)
    
    def query(self, i) -> int:
        """Get prefix sum up to index i."""
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= i & (-i)
        return result
    
    def range_query(self, left, right) -> int:
        """Get sum of elements from left to right (inclusive)."""
        return self.query(right) - self.query(left - 1)


class SegmentTree:
    """
    Segment Tree for range queries (min/max/sum).
    Time: O(log n) for query and update, Space: O(4n)
    """
    
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2 * node + 1, start, mid)
            self.build(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
    
    def query(self, node, start, end, left, right) -> int:
        """Range sum query from left to right."""
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        
        mid = (start + end) // 2
        p1 = self.query(2 * node + 1, start, mid, left, right)
        p2 = self.query(2 * node + 2, mid + 1, end, left, right)
        return p1 + p2
    
    def range_query(self, left, right) -> int:
        return self.query(0, 0, self.n - 1, left, right)


class SuffixArray:
    """
    Suffix Array for efficient substring search.
    Time: O(n log n) to build, O(log n) to search, Space: O(n)
    """
    
    def __init__(self, text: str):
        self.text = text
        self.suffix_array = self._build_suffix_array()
    
    def _build_suffix_array(self):
        suffixes = [(self.text[i:], i) for i in range(len(self.text))]
        suffixes.sort()
        return [suffix[1] for suffix in suffixes]
    
    def search(self, pattern: str) -> List[int]:
        """Search for pattern using binary search on suffix array."""
        def compare_with_pattern(suffix_index, pattern):
            suffix = self.text[suffix_index:suffix_index + len(pattern)]
            if suffix < pattern:
                return -1
            elif suffix > pattern:
                return 1
            else:
                return 0
        
        # Find leftmost occurrence
        left, right = 0, len(self.suffix_array) - 1
        start = -1
        
        while left <= right:
            mid = (left + right) // 2
            cmp = compare_with_pattern(self.suffix_array[mid], pattern)
            
            if cmp == 0:
                start = mid
                right = mid - 1
            elif cmp < 0:
                left = mid + 1
            else:
                right = mid - 1
        
        if start == -1:
            return []
        
        # Find rightmost occurrence
        left, right = 0, len(self.suffix_array) - 1
        end = -1
        
        while left <= right:
            mid = (left + right) // 2
            cmp = compare_with_pattern(self.suffix_array[mid], pattern)
            
            if cmp == 0:
                end = mid
                left = mid + 1
            elif cmp < 0:
                left = mid + 1
            else:
                right = mid - 1
        
        # Return all occurrences
        return [self.suffix_array[i] for i in range(start, end + 1)]


class SkipListNode:
    def __init__(self, val, level):
        self.val = val
        self.forward = [None] * (level + 1)


class SkipList:
    """
    Skip List - probabilistic data structure.
    Time: O(log n) average, O(n) worst, Space: O(n)
    """
    
    def __init__(self, max_level=16, p=0.5):
        self.max_level = max_level
        self.p = p
        self.header = SkipListNode(-1, max_level)
        self.level = 0
    
    def random_level(self):
        level = 0
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level
    
    def search(self, target) -> bool:
        """Search for target in skip list."""
        current = self.header
        
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].val < target:
                current = current.forward[i]
        
        current = current.forward[0]
        return current is not None and current.val == target
    
    def insert(self, val):
        """Insert value into skip list."""
        update = [None] * (self.max_level + 1)
        current = self.header
        
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].val < val:
                current = current.forward[i]
            update[i] = current
        
        current = current.forward[0]
        
        if current is None or current.val != val:
            new_level = self.random_level()
            
            if new_level > self.level:
                for i in range(self.level + 1, new_level + 1):
                    update[i] = self.header
                self.level = new_level
            
            new_node = SkipListNode(val, new_level)
            
            for i in range(new_level + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node


# =============================================================================
# TEST FUNCTIONS AND EXAMPLES
# =============================================================================

def test_search_algorithms():
    """Test all search algorithms with sample data."""
    
    print("🔍 Testing Search Algorithms")
    print("=" * 50)
    
    # Test data
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    unsorted_array = [64, 34, 25, 12, 22, 11, 90]
    target = 11
    
    # LINEAR SEARCH TESTS
    print("\n📏 LINEAR SEARCH ALGORITHMS")
    print("-" * 30)
    
    result = linear_search(unsorted_array, target)
    print(f"Linear Search: Found {target} at index {result}")
    
    result = sentinel_linear_search(unsorted_array.copy(), target)
    print(f"Sentinel Linear Search: Found {target} at index {result}")
    
    # BINARY SEARCH TESTS
    print("\n🔄 BINARY SEARCH ALGORITHMS")
    print("-" * 30)
    
    result = binary_search_iterative(sorted_array, target)
    print(f"Binary Search (Iterative): Found {target} at index {result}")
    
    result = binary_search_recursive(sorted_array, target)
    print(f"Binary Search (Recursive): Found {target} at index {result}")
    
    result = exponential_search(sorted_array, target)
    print(f"Exponential Search: Found {target} at index {result}")
    
    result = interpolation_search(sorted_array, target)
    print(f"Interpolation Search: Found {target} at index {result}")
    
    result = ternary_search(sorted_array, target)
    print(f"Ternary Search: Found {target} at index {result}")
    
    # JUMP SEARCH TESTS
    print("\n🦘 JUMP/BLOCK SEARCH ALGORITHMS")
    print("-" * 30)
    
    result = jump_search(sorted_array, target)
    print(f"Jump Search: Found {target} at index {result}")
    
    result = fibonacci_search(sorted_array, target)
    print(f"Fibonacci Search: Found {target} at index {result}")
    
    # TREE SEARCH TESTS
    print("\n🌳 TREE-BASED SEARCH")
    print("-" * 30)
    
    # BST Test
    bst = BST()
    for val in [15, 10, 20, 8, 12, 25, 6, 11, 13, 27]:
        bst.insert(val)
    
    result = bst.search(target)
    print(f"Binary Search Tree: Found {target}: {result}")
    
    # Trie Test
    trie = Trie()
    words = ["hello", "world", "help", "hero", "search"]
    for word in words:
        trie.insert(word)
    
    result = trie.search("help")
    print(f"Trie Search: Found 'help': {result}")
    
    result = trie.starts_with("hel")
    print(f"Trie Prefix Search: Words starting with 'hel': {result}")
    
    # HASH-BASED SEARCH TESTS
    print("\n# HASH-BASED SEARCH")
    print("-" * 30)
    
    # Hash Table Test
    hash_table = HashTable()
    hash_table.insert("key1", "value1")
    hash_table.insert("key2", "value2")
    hash_table.insert("search", "found!")
    
    result = hash_table.search("search")
    print(f"Hash Table Search: Found 'search': {result}")
    
    # Bloom Filter Test
    bloom = BloomFilter(size=100, hash_count=3)
    test_items = ["apple", "banana", "orange", "grape"]
    for item in test_items:
        bloom.add(item)
    
    result = bloom.contains("apple")
    print(f"Bloom Filter: Contains 'apple': {result}")
    
    result = bloom.contains("pear")
    print(f"Bloom Filter: Contains 'pear': {result} (might be false positive)")
    
    # GRAPH SEARCH TESTS
    print("\n🕸️ GRAPH SEARCH ALGORITHMS")
    print("-" * 30)
    
    # Create test graph
    graph = Graph()
    edges = [('A', 'B', 1), ('A', 'C', 4), ('B', 'C', 2), ('B', 'D', 5), 
             ('C', 'D', 1), ('D', 'E', 3)]
    
    for u, v, w in edges:
        graph.add_edge(u, v, w)
        graph.add_edge(v, u, w)  # Make it undirected
    
    # BFS Test
    path = graph.bfs('A', 'E')
    print(f"BFS path from A to E: {path}")
    
    # DFS Test
    path = graph.dfs('A', 'E')
    print(f"DFS path from A to E: {path}")
    
    # Dijkstra Test
    distance, path = graph.dijkstra('A', 'E')
    print(f"Dijkstra shortest path A to E: {path} (distance: {distance})")
    
    # A* Test (simple grid heuristic)
    def manhattan_distance(a, b):
        # Simple heuristic for demonstration
        return abs(ord(a) - ord(b))
    
    simple_graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C', 'E'],
        'E': ['D']
    }
    
    path = a_star_search(simple_graph, 'A', 'E', manhattan_distance)
    print(f"A* path from A to E: {path}")
    
    # STRING SEARCH TESTS
    print("\n📝 STRING SEARCH ALGORITHMS")
    print("-" * 30)
    
    text = "ABABDABACDABABCABCABCABCABC"
    pattern = "ABABCAB"
    
    positions = naive_string_search(text, pattern)
    print(f"Naive String Search: Pattern '{pattern}' found at positions: {positions}")
    
    positions = kmp_search(text, pattern)
    print(f"KMP Search: Pattern '{pattern}' found at positions: {positions}")
    
    positions = boyer_moore_search(text, pattern)
    print(f"Boyer-Moore Search: Pattern '{pattern}' found at positions: {positions}")
    
    positions = rabin_karp_search(text, pattern)
    print(f"Rabin-Karp Search: Pattern '{pattern}' found at positions: {positions}")
    
    # SPECIALIZED SEARCH TESTS
    print("\n⚡ SPECIALIZED SEARCH ALGORITHMS")
    print("-" * 30)
    
    # QuickSelect Test
    test_array = [3, 6, 8, 10, 1, 2, 1]
    k = 3  # Find 3rd smallest (0-indexed)
    result = quickselect(test_array, k)
    print(f"QuickSelect: {k}th smallest element in {test_array}: {result}")
    
    # Binary Indexed Tree Test
    bit = BinaryIndexedTree(10)
    values = [1, 3, 5, 7, 9, 11]
    for i, val in enumerate(values, 1):
        bit.update(i, val)
    
    range_sum = bit.range_query(2, 4)
    print(f"Binary Indexed Tree: Sum of range [2,4]: {range_sum}")
    
    # Segment Tree Test
    seg_tree = SegmentTree([1, 3, 5, 7, 9, 11])
    range_sum = seg_tree.range_query(1, 3)
    print(f"Segment Tree: Sum of range [1,3]: {range_sum}")
    
    # Suffix Array Test
    text = "banana"
    suffix_array = SuffixArray(text)
    positions = suffix_array.search("ana")
    print(f"Suffix Array: Pattern 'ana' found at positions: {positions}")
    
    # Skip List Test
    skip_list = SkipList()
    values = [3, 6, 7, 9, 12, 19, 17, 26, 21, 25]
    for val in values:
        skip_list.insert(val)
    
    found = skip_list.search(12)
    print(f"Skip List: Found 12: {found}")
    
    found = skip_list.search(15)
    print(f"Skip List: Found 15: {found}")


def performance_comparison():
    """Compare performance of different search algorithms."""
    import time
    
    print("\n⏱️ PERFORMANCE COMPARISON")
    print("=" * 50)
    
    # Generate test data
    sizes = [1000, 10000, 100000]
    
    for size in sizes:
        print(f"\nArray size: {size:,}")
        print("-" * 20)
        
        # Create sorted array
        arr = list(range(0, size * 2, 2))
        target = size  # Middle element
        
        # Linear Search
        start = time.time()
        result = linear_search(arr, target)
        linear_time = time.time() - start
        
        # Binary Search
        start = time.time()
        result = binary_search_iterative(arr, target)
        binary_time = time.time() - start
        
        # Jump Search
        start = time.time()
        result = jump_search(arr, target)
        jump_time = time.time() - start
        
        print(f"Linear Search:  {linear_time:.6f} seconds")
        print(f"Binary Search:  {binary_time:.6f} seconds")
        print(f"Jump Search:    {jump_time:.6f} seconds")
        
        if binary_time > 0:
            print(f"Binary vs Linear speedup: {linear_time/binary_time:.1f}x")


def complexity_examples():
    """Demonstrate time complexity differences with examples."""
    
    print("\n📊 COMPLEXITY EXAMPLES")
    print("=" * 50)
    
    print("\n🎯 Best Use Cases for Each Algorithm:")
    print("-" * 40)
    
    examples = [
        ("Linear Search", "Small unsorted arrays, linked lists, one-time searches"),
        ("Binary Search", "Large sorted arrays, frequent searches, range queries"),
        ("Hash Table", "Fast key-value lookups, caches, symbol tables"),
        ("Trie", "Autocomplete, spell checkers, IP routing tables"),
        ("BFS", "Shortest path in unweighted graphs, level-order traversal"),
        ("DFS", "Maze solving, topological sorting, cycle detection"),
        ("A*", "Game pathfinding, GPS navigation, puzzle solving"),
        ("KMP", "Pattern matching in DNA sequences, text editors"),
        ("Suffix Array", "Finding all occurrences of patterns, bioinformatics"),
        ("Bloom Filter", "Database query optimization, web caching")
    ]
    
    for algorithm, use_case in examples:
        print(f"{algorithm:15}: {use_case}")
    
    print("\n💡 Performance Tips:")
    print("-" * 20)
    tips = [
        "Always use binary search on sorted data",
        "Hash tables are fastest for exact key lookups",
        "Use tries for prefix-based searches",
        "Consider space-time tradeoffs",
        "Preprocessing can improve query performance",
        "Choose algorithms based on data characteristics",
        "Cache-friendly algorithms perform better in practice"
    ]
    
    for i, tip in enumerate(tips, 1):
        print(f"{i}. {tip}")


if __name__ == "__main__":
    # Run all tests
    test_search_algorithms()
    performance_comparison()
    complexity_examples()
    
    print("\n✅ All search algorithm implementations completed!")
    print("\nTo use any algorithm:")
    print("1. Import the functions you need")
    print("2. Prepare your data (sort if needed)")
    print("3. Call the appropriate search function")
    print("4. Handle the returned result")
    
    print("\n📚 Example usage:")
    print("arr = [1, 3, 5, 7, 9, 11, 13, 15]")
    print("index = binary_search_iterative(arr, 7)")
    print("print(f'Found at index: {index}')")
    
    print("\n🔗 For more complex data structures:")
    print("bst = BST()")
    print("bst.insert(10)")
    print("found = bst.search(10)")
    
    print("\n🌐 For graph problems:")
    print("graph = Graph()")
    print("graph.add_edge('A', 'B')")
    print("path = graph.bfs('A', 'B')")