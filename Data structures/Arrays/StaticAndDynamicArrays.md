# Static Array vs Dynamic Array

### 1. **Static Array**

* **Definition:**
  A static array is an array with a **fixed size** determined when it is created.
  You **cannot change its size** after creation.

* **Memory:**
  Allocated as a **contiguous block** of memory with a fixed length.

* **Example:**
  In languages like C or C++:

  ```c
  int arr[5]; // An array of 5 integers, size fixed at 5
  ```

* **Advantages:**

  * Fast access: O(1) time for any element because elements are stored continuously.
  * Simple memory management (no resizing).

* **Disadvantages:**

  * Fixed size can waste memory if array is not full.
  * Cannot grow or shrink during runtime.

---

### 2. **Dynamic Array**

* **Definition:**
  A dynamic array can **change size during runtime** — you can add or remove elements.

* **Memory:**
  Implemented with a **contiguous block** of memory that can be resized.
  When capacity is exceeded, a **new bigger block** is allocated, and elements are copied over.

* **Example:**
  Python’s `list`, Java’s `ArrayList`, C++ `vector`.

* **Advantages:**

  * Flexible size; can grow or shrink.
  * Fast random access: O(1).

* **Disadvantages:**

  * Resizing can be costly (copying elements to a new memory block).
  * Slight overhead for tracking size and capacity.

---

### **Summary Table**

| Feature       | Static Array                             | Dynamic Array                             |
| ------------- | ---------------------------------------- | ----------------------------------------- |
| Size          | Fixed at creation                        | Can grow or shrink at runtime             |
| Memory        | Contiguous, fixed size                   | Contiguous, resized when needed           |
| Access Time   | O(1)                                     | O(1)                                      |
| Insert/Delete | Expensive if not at end (shift elements) | Amortized O(1) append; O(n) insert/delete |
| Use Case      | When size is known & fixed               | When size can vary                        |

---