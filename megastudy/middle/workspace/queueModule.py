#!/usr/bin/env python
# coding: utf-8

# # 큐(Queue)

# In[52]:


class Queue:

    def __init__(self, size=5):
        self.queue = []  # 큐 역할을 할 빈 리스트
        self.size = size  # 큐의 크기
        self.rear = 0  # 큐의 뒤쪽 포인터 → 큐에 데이터가 입력될 때마다 1씩 증가한다.
        self.front = 0  # 큐의 앞쪽 포인터 → 큐에서 데이터가 제거될 때마다 1씩 증가한다.

    # add(입력)
    def add(self, data):
        if data not in self.queue:  # 중복 검사
            if self.rear < self.size:  # Overflow 검사
                self.queue.append(data)
                # 큐에 데이터를 추가했으므로 rear를 1 증가시킨다.
                self.rear += 1
                print(f'큐에 {data}을(를) 저장합니다. [rear = {self.rear}, front = {self.front}]')
            else:
                print(f'Overflow 발생! 큐가 가득 차서 {data}를 저장할 수 없습니다.')
        else:
            print(f'{data}는 중복된 데이터입니다.')
        self.view()

    # view(데이터 보기)
    def view(self):
        print('큐에 저장된 데이터: ', end='')
        # Underflow인지 검사한다. 큐의 Underflow 조건은 2가지가 존재한다.
        # 1. 데이터가 한 건도 입력되지 않았을 경우 rear == 0 이므로 Underflow가 발생한다.
        # 2. 데이터가 모두 제거된 경우 rear == front 이므로 Underflow가 발생한다.
        if self.rear <= 0 or self.rear <= self.front:
            print('없음')
        else:
            # 큐에 저장된 데이터의 개수 만큼 반복하며 큐에 저장된 데이터를 출력한다.
            # for i in range(self.front, self.rear):
            for q in self.queue[self.front:]:
                print(q, end=' ')
            print()

    # remove(출력)
    def remove(self):
        # Underflow인지 검사한다.
        if self.rear <= 0 or self.rear <= self.front:
            print('큐에 저장된 데이터가 없습니다.')
        else:
            # 큐에 저장된 제거할 데이터를 얻어온다.
            data = self.queue[self.front]
            # 얻어온 데이터를 큐에서 제거한다.
            self.queue[self.front] = '제거됨'
            # 큐에서 데이터를 제거했으므로 front를 1 증가시킨다.
            self.front += 1
            print(f'큐에서 {data}을(를) 제거합니다. [rear = {self.rear}, front = {self.front}]')
            # self.view()


# In[53]:


if __name__ == '__main__':
    queue = Queue()
    queue.view()
    queue.add(0)
    queue.add(1)
    queue.add(2)
    queue.add(3)
    queue.add(4)
    queue.add(5)
    print('=' * 80)
    queue.view()
    print('=' * 80)
    queue.remove()
    queue.remove()
    queue.remove()
    queue.remove()
    queue.remove()
    queue.remove()


# In[33]:




