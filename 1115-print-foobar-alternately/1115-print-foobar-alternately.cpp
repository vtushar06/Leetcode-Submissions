#include <mutex>
#include <condition_variable>
#include <functional>

using namespace std;

class FooBar {
private:
    int n;
    mutex mtx;
    condition_variable cv;
    bool foo_turn;

public:
    FooBar(int n) {
        this->n = n;
        this->foo_turn = true; // "foo" must always go first
    }

    void foo(function<void()> printFoo) {
        for (int i = 0; i < n; i++) {
            // Acquire the lock
            unique_lock<mutex> lock(mtx);
            
            // Wait until it is foo's turn. 
            // If foo_turn is false, this thread releases the lock and sleeps.
            cv.wait(lock, [this]() { return foo_turn; });
            
            // printFoo() outputs "foo". Do not change or remove this line.
            printFoo();
            
            // Hand the baton to bar
            foo_turn = false;
            
            // Wake up the other thread waiting on this condition variable
            cv.notify_one();
        }
    }

    void bar(function<void()> printBar) {
        for (int i = 0; i < n; i++) {
            // Acquire the lock
            unique_lock<mutex> lock(mtx);
            
            // Wait until foo_turn is false
            cv.wait(lock, [this]() { return !foo_turn; });
            
            // printBar() outputs "bar". Do not change or remove this line.
            printBar();
            
            // Hand the baton back to foo
            foo_turn = true;
            
            // Wake up the other thread
            cv.notify_one();
        }
    }
};