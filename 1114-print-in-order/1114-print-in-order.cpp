#include <mutex>
#include <condition_variable>
using namespace std;

class Foo {
private:
    mutex mtx;
    condition_variable cv;
    int step;  // keeps track of which function should run

public:
    Foo() {
        step = 1; // first() should run first
    }

    void first(function<void()> printFirst) {
        unique_lock<mutex> lock(mtx);
        // printFirst() outputs "first".
        printFirst();
        step = 2;       // allow second() to run
        cv.notify_all(); // wake up waiting threads
    }

    void second(function<void()> printSecond) {
        unique_lock<mutex> lock(mtx);
        cv.wait(lock, [this]() { return step == 2; }); // wait until first() finishes
        printSecond();
        step = 3;       // allow third() to run
        cv.notify_all();
    }

    void third(function<void()> printThird) {
        unique_lock<mutex> lock(mtx);
        cv.wait(lock, [this]() { return step == 3; }); // wait until second() finishes
        printThird();
    }
};