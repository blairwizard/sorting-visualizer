import pygame
import random
pygame.init()
global values, barh, sorter, i, j
sorting = False
WINDOW_SIZE = 600
H=800
i,j=0,0
values=[random.randint(1,100) for i in range(50)]
barw=(WINDOW_SIZE//len(values))
barh=((H-200)//max(values))
screen = pygame.display.set_mode((WINDOW_SIZE, H))
pygame.display.set_caption("Sorting Visualization")
font = pygame.font.SysFont("Arial", 20)
bubble_btn = pygame.Rect(10, 10, 150, 40)
merge_btn = pygame.Rect(170, 10, 150, 40)
reset_btn = pygame.Rect(330, 10, 150, 40)
start_btn = pygame.Rect(490, 10, 100, 40)
quick_btn = pygame.Rect(10, 60, 150, 40)
exit_btn= pygame.Rect(170, 60, 150, 40)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp

    # place pivot in correct position
    temp = arr[i+1]
    arr[i+1] = arr[high]
    arr[high] = temp

    return i + 1


def quick_sort(arr, low, high):
    if low >= high:  # base case
        return

    pivot_idx = partition(arr, low, high)
    yield from quick_sort(arr, low, pivot_idx - 1)  # sort left
    yield from quick_sort(arr, pivot_idx + 1, high)  # sort right
    yield low, high  # for visualization

def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                yield j,j+1


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])  # ← this is the else block
            j += 1

    result += left[i:]
    result += right[j:]
    return result


def merge_sort(arr, left, right):
    if left >= right:
        return

    mid = (left + right) // 2
    yield from merge_sort(arr, left, mid)        # ← replace merge_sort(arr, left, mid)
    yield from merge_sort(arr, mid + 1, right)   # ← replace merge_sort(arr, mid + 1, right)

    merged = merge(arr[left:mid + 1], arr[mid + 1:right + 1])
    arr[left:right + 1] = merged
    yield left, right   # ← add this line

sorter=merge_sort(values, 0, len(values)-1)
clock = pygame.time.Clock()
running= True
while running:
    if sorting:
        try:
            i, j = next(sorter)
        except StopIteration:
            sorting = False

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_q:
                running=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if start_btn.collidepoint(mouse_x, mouse_y):
                sorting = True
            if bubble_btn.collidepoint(mouse_x, mouse_y):
                values = [random.randint(1, 100) for _ in range(50)]
                sorter = bubble_sort(values)
                i, j = 0, 0
            if merge_btn.collidepoint(mouse_x, mouse_y):
                values = [random.randint(1, 100) for _ in range(50)]
                sorter = merge_sort(values, 0, len(values) - 1)
                i, j = 0, 0
            if reset_btn.collidepoint(mouse_x, mouse_y):
                values = [random.randint(1, 100) for _ in range(50)]
                sorter = iter([])
                i, j = 0, 0
            if quick_btn.collidepoint(mouse_x, mouse_y):
                values = [random.randint(1, 100) for _ in range(50)]
                sorter = quick_sort(values, 0, len(values) - 1)
                i, j = 0, 0
            if exit_btn.collidepoint(mouse_x, mouse_y):
                running = False
    screen.fill((0,0,0))
    # draw buttons
    pygame.draw.rect(screen, "green", start_btn)
    screen.blit(font.render("Start", True, "white"), (start_btn.x + 25, start_btn.y + 10))
    pygame.draw.rect(screen, "blue", bubble_btn)
    pygame.draw.rect(screen, "blue", merge_btn)
    pygame.draw.rect(screen, "orange", reset_btn)
    pygame.draw.rect(screen,"yellow", quick_btn)
    pygame.draw.rect(screen,"red", exit_btn)

    # draw button labels
    screen.blit(font.render("Bubble Sort", True, "white"), (bubble_btn.x + 10, bubble_btn.y + 10))
    screen.blit(font.render("Merge Sort", True, "white"), (merge_btn.x + 10, merge_btn.y + 10))
    screen.blit(font.render("Reset", True, "white"), (reset_btn.x + 45, reset_btn.y + 10))
    screen.blit(font.render("Quick Sort",True,"black"), (quick_btn.x + 10, quick_btn.y + 10))
    screen.blit(font.render("Exit", True, "black"), (exit_btn.x + 45, exit_btn.y + 10))
    for k in range(len(values)):
        bh = values[k] * barh
        x = k * barw
        y = H - bh
        if i <= k <= j:
            color = "red"
        else:
            color = "green"
        pygame.draw.rect(screen, color, (x, y, barw, bh))
        pygame.draw.rect(screen,"black", (x, y, barw, bh),1)
    pygame.display.flip()
    clock.tick(40)

pygame.quit()

