#include <iostream>
#include <chrono>
using namespace std;

const int ARRAY_SIZE = 50000;

void arrayStatic();
void arrayStackDynamic();
void arrayHeapDynamic();

int main(void) {

 auto start = chrono::high_resolution_clock::now();
 arrayStatic();
 auto end = chrono::high_resolution_clock::now();
 printf("array static: %f\n", chrono::duration_cast<chrono::nanoseconds>(end - start).count()*1e-9);

 start = chrono::high_resolution_clock::now();
 arrayStackDynamic();
 end = chrono::high_resolution_clock::now();
 printf("array stack dynamic: %f\n", chrono::duration_cast<chrono::nanoseconds>(end - start).count() * 1e-9);

 start = chrono::high_resolution_clock::now();
 arrayHeapDynamic();
 end = chrono::high_resolution_clock::now();
 printf("array heap dynamic: %f\n", chrono::duration_cast<chrono::nanoseconds>(end - start).count() * 1e-9);


 return 0;
}

void arrayStatic(){
  static int arr[ARRAY_SIZE];
  //init array
}

void arrayStackDynamic(){
  int arr[ARRAY_SIZE];
   //init array
}

void arrayHeapDynamic(){
  int* arr = new int[ARRAY_SIZE];
   //init array
}
