class DynamicArray {
private: 
    int *arr;
    int capacity;
    int size;
public:

    DynamicArray(int capacity) {
        if(capacity > 0){
            this->capacity = capacity;
            this->arr = new int[capacity];
            this->size = 0;
        }

    }

    int get(int i) {
        return this->arr[i];
    }

    void set(int i, int n) {
        this->arr[i] = n;
    }

    void pushback(int n) {
        if(size >= capacity){
            // resize
            resize(capacity * 2);
            this->arr[size] = n;
            this->size += 1;
        }
        else{
            this->arr[size] = n;
            this->size += 1;
        }
    }

    int popback() {
        this->size -= 1;
        return this->arr[size];
    }

    void resize(int newCapacity) {
        int *resizedArr = new int[newCapacity];
        // loop through all the pointer values and reassign to this new
        int i = 0;
        while(i <= this->capacity){
            resizedArr[i] = this->arr[i];
            i++;
        }
        delete[] arr;
        this->arr = resizedArr; 
        this->capacity = newCapacity;
    }

    int getSize() {
        return this->size;
    }

    int getCapacity() {
        return this->capacity;
    }

    ~DynamicArray() {
        delete[] arr;
    }
};
