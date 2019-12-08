#include "stack.h"

int main()
{
	struct Stack *stack = createStack(100);

	push(stack, 55);
	push(stack, 11);

	printf("%d popped from stack\n", pop(stack));

	return 0;
}
