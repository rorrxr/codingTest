#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int main() {
	
	int input_m;
	int input_day;

	scanf("%d", &input_m);
	scanf("%d", &input_day);

	//이전
	if (input_m < 2){
		printf("Before");

	}
	
	else if (input_m == 2) {
		if (input_day < 18)
			printf("Before");
		else if (input_day > 18)
			printf("After");
		else
			printf("Special");
	}
	else
		printf("After");

	return 0;
}