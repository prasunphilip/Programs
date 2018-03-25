#include<dos.h>
#include<stdio.h>
#include<conio.h>
void intrr();
void main()
{	int a,b,c=0;
	clrscr();
	printf("Enter the first number: ");
	scanf("%d",&a);
	printf("Enter the second number: ");
	scanf("%d",&b);
	intrr();
	delay(1200);
	printf("Interrupt Handled\n");
	c=a+b;
	printf("Sum = %d",c);
	getch();
}
void intrr()
{
	char *message = "Handling Interrupt\n$";
	_AH = 9;
	_DX = (int) message;
	geninterrupt(0x21);
}