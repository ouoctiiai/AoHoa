#include <stdio.h>

int main() {
    printf("Cac so nguyen co 2 chu so va la boi cua 7:\n");

    // Duyệt qua tất cả các số từ 10 đến 99
    for (int i = 10; i <= 99; i++) {
        // Kiểm tra nếu số đó là bội của 7
        if (i % 7 == 0) {
            printf("%d\n", i);
        }
    }

    return 0;
}
