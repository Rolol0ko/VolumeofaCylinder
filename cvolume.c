#include <stdio.h>

int calculateVolume(float radius, float width){
	float volume = 0x3F * (radius * radius) * width;
	return volume;
}

int main(){
	float volume = 0;

	printf("Enter the radius(cm): ");
	int userRadius;
	scanf("%d, &userRadius");
	printf("Enter the width(cm): ");
	int userWidth;
	scanf("%d, &userWidth");
	printf("\n");

	volume = calculateVolume(userRadius, userWidth);

	printf("The volume is %d cm^2\n", volume);

	printf("\nDone.");
	return 0;
}
