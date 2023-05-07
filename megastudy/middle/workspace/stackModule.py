#!/usr/bin/env python
# coding: utf-8

# # 스택

# In[40]:


class Stack:
    # Stack 클래스가 생성될 때 스택의 크기를 넘겨받으면 해당 스택 크기 만큼의 기억공간을 가지는 스택을 생성하고, 스택 크기를 넘겨받지 않으면 5개의 데이터를 저장할 수 있는 스택을 만든다. → 디폴트 인수 사용
    def __init__(self, size=5):
        # print(f'스택의 크기: {size}')
        # 초기자 함수에서 스택으로 사용할 빈 리스트를 만든다.
        self.stack = []  # stack → 빈 리스트 → 데이터는 append() 메서드로 추가한다.
        self.size = size  # 스택의 크기
        # top(SP, Stack Pointer): 스택에 몇 개의 데이터가 저장되었는지 기억한다.
        # 데이터가 입력되면 1 증가, 데이터가 출력되면 1 감소 → 스택의 크기와 비교해서 Overflow/Underflow를 처리한다.
        self.top = 0

    # push(입력)
    def push(self, data):
        if data not in self.stack:  # 스택에 저장하려는 데이터가 스택에 존재하지 않을 때
            # 스택에 저장하려는 데이터가 스택에 존재하지 않으므로 저장하기 전에 Overflow인지 검사한다.
            # 스택의 크기가 5일 때 스택으로 사용할 리스트의 인덱스는 0, 1, 2, 3, 4만 사용할 수 있다.
            if self.top < self.size:
                # Overflow가 발생되지 않았으므로 스택에 데이터를 저장한다.
                self.stack.append(data)
                self.top += 1
                # print(self.stack)
            else:
                # Overflow가 발생되면 스택이 가득 찼다는 메시지를 출력한다.
                print(f'Overflow 발생! 스택이 가득 차서 {data}을(를) 저장할 수 없습니다.')
                # print(self.stack)
        else:
            print(f'{data}는 중복된 데이터입니다.')
            # print(self.stack)
        # 스택에 저장된 데이터를 출력하는 함수(view)를 실행한다.
        # 현재 클래스 내부에 다른 함수를 실행하려는 경우 앞에 'self'를 붙여서 실행해야 한다.
        self.view()

    # view(보기): 스택에 저장된 데이터를 출력한다.
    def view(self):
        print('스택에 저장된 데이터: ', end='')
        # Underflow인지 검사한다.
        if self.top <= 0:
            print('없음')
        else:
            # 스택에 저장된 데이터의 개수 만큼 반복하며 스택에 저장된 데이터를 출력한다.
            # for i in range(len(self.stack)):
            # for i in range(self.top):
            #     print(self.stack[i], end=' ')
            for s in self.stack:
                print(s, end=' ')
            print()

    # pop(출력)
    def pop(self):
        # Underflow인지 검사한다.
        if self.top <= 0:
            print('스택에 저장된 데이터가 없습니다.')
        else:
            # 파이썬 리스트 메서드 중에서 pop() 메서드를 사용해서 스택에 저장된 데이터를 얻어온 후 리스트에서 제거한다.
            print(f'스택에서 제거된 데이터: {self.stack.pop()}')
            # 스택에 저장된 데이터가 출력되었으므로 top을 1 감소시킨다.
            self.top -= 1
            self.view()


# In[41]:


if __name__ == '__main__':
    stack = Stack()
    stack.view()
    stack.pop()
    stack.push(2022)
    stack.push(2022)
    stack.push('DEC')
    stack.push('7th')
    stack.push('13h')
    stack.push('13m')
    print('=' * 80)
    stack.view()
    print('=' * 80)
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.view()


# In[ ]:




