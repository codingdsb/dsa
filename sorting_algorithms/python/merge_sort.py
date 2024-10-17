def merge_sort(numbers):
    length = len(numbers)
    nums1 = numbers[:length//2]
    nums2 = numbers[length//2:]
    if len(nums1) == 1 and len(nums2) == 1:
        return merge(nums1, nums2)
    elif len(nums1) == 1 and len(nums2) == 2:
        sorted_nums2 = merge_sort(nums2)
        return merge(nums1, sorted_nums2)

    sorted_nums1 = merge_sort(nums1)
    sorted_nums2 = merge_sort(nums2)

    return merge(sorted_nums1, sorted_nums2)

def merge(nums1, nums2):
    i = 0
    j = 0
    merged = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    while i < len(nums1):
        merged.append(nums1[i])
        i += 1
    while j < len(nums2):
        merged.append(nums2[j])
        j += 1

    return merged

print(merge_sort([3,4, 7, 2,1]))