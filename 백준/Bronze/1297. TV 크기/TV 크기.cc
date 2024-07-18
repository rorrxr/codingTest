#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<math.h>
#include<cmath>

int main() {
	int diag;
	int width;
	int height;

	double r_diag;
	double r_width;
	double r_height;

	//대각선 길이, 높이 비율, 너비 비율 입력
	scanf("%d %d %d", &diag, &height, &width);

	r_diag = sqrt((height*height) + (width*width));

	r_height = diag * height / r_diag;
	r_width = diag * width / r_diag;

	//tv의 높이/ tv의 너비 출력
	printf("%d %d", int(r_height), int(r_width));

	return 0;
}