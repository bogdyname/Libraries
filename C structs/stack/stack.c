#include "stack.h"

struct Stack *createStack(unsigned capacity)
{
	struct Stack *stack = (struct Stack *)malloc(sizeof(struct Stack));
	stack->capacity = capacity;
	stack->topElement = -1;
	stack->data = (int*)malloc(stack->capacity * sizeof(int));
	//here it's test, but not done at all
	
	return stack;
}

int isFull(struct Stack *stack)
{
	return stack->topElement == stack->capacity -1;
}

int isEmpty(struct Stack *stack)
{
	return stack->topElement == -1;
}

void push(struct Stack *stack, int item)
{
	if(isFull(stack))
		return;

	stack->data[++stack->topElement] = item;
}

int pop(struct Stack *stack)
{

	return stack->data[stack->topElement--];
}

int peek(struct Stack *stack)
{
	if(isEmpty(stack))
		return INT_MIN;

	return stack->data[stack->topElement];
}
