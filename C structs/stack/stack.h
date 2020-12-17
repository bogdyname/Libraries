#ifndef STACK_H
#define STACK_H

#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

struct Stack
{
	int topElement;
	unsigned capacity;
	int* data; //past here template of data
	//now it's test with int
};


struct Stack *createStack(unsigned capacity);
int pop(struct Stack *stack);
int peek(struct Stack *stack);
int isFull(struct Stack *stack);
int isEmpty(struct Stack *stack);
void push(struct Stack *stack, int item);

#endif
