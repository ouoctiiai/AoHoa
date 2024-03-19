#include <stdio.h>
#include <math.h>

// Hàm kiểm tra số chính phương
int isPerfectSquare(int num) {
    int squareRoot = sqrt(num);
    return squareRoot * squareRoot == num;
}

// Hàm đếm và in ra các số chính phương nhỏ hơn n
int printPerfectSquares(int n) {
    int count = 0;
    printf("Cac so chinh phuong nho hon %d:\n", n);
    for (int i = 1; i < n; i++) {
        if (isPerfectSquare(i)) {
            count++;
            printf("%d ", i);
        }
    }
    printf("\n");
    return count;
}

int main() {
    int n;
    scanf("%d", &n);

    // Gọi hàm để in ra các số chính phương nhỏ hơn n
    int count = printPerfectSquares(n);
    printf("So luong so chinh phuong nho hon %d la: %d\n", n, count);

    return 0;
}
