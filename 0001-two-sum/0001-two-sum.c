#include <stdlib.h>

#define TABLE_SIZE 10007

typedef struct {
    int key;
    int val;
    int used;
} HashEntry;

int hash(int key) {
    int h = key % TABLE_SIZE;
    if (h < 0) h += TABLE_SIZE;
    return h;
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    HashEntry table[TABLE_SIZE] = {0};
    
    int* result = (int*)malloc(2 * sizeof(int));
    *returnSize = 2;

    for (int i = 0; i < numsSize; i++) {
        int diff = target - nums[i];
        int idx = hash(diff);
        while (table[idx].used) {
            if (table[idx].key == diff) {
                result[0] = table[idx].val;
                result[1] = i;
                return result;
            }
            idx = (idx + 1) % TABLE_SIZE;
        }
        idx = hash(nums[i]);
        while (table[idx].used) {
            idx = (idx + 1) % TABLE_SIZE;
        }
        table[idx].key = nums[i];
        table[idx].val = i;
        table[idx].used = 1;
    }

    *returnSize = 0;
    return NULL;
}