#!/usr/bin/env python
# coding: utf-8

# # Selection Sort(선택 정렬, 교환법) 알고리즘
# 선택 정렬은 i번째 데이터를 선택해서 나머지 데이터(j번째)와 비교하며 정렬한다.
# 정렬할 데이터가 n개일 경우 회전수는 (n - 1)번가 된다. → 데이터가 5개면 회전수는 4번이다.
# <br/>
# <img src="./images/selectionSort1.png"/>
# <br/>
# <img src="./images/selectionSort2.png"/>
# <br/>
# <img src="./images/selectionSort3.png"/>

# In[18]:


'''
n = 5
for i in range(n - 1):
    for j in range(i + 1, n):
        print('[i = {}, j = {}]'.format(i, j), end='')
    print()
'''
pass


# In[34]:


data = [8, 3, 4, 9, 1]


# In[33]:


def selection_sort_asc(data):
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
            # ===== if
        # ===== for j: 회전 종료
        # print('{}회전 결과: {}'.format(i + 1, data))
    # ===== for i: 정렬 종료
    # print(f'정렬 결과: {data}')
    return data


selection_sort_asc(data)


# In[26]:


def selection_sort_desc(data):
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            if data[i] < data[j]:
                data[i], data[j] = data[j], data[i]
            # ===== if
        # ===== for j: 회전 종료
        # print('{}회전 결과: {}'.format(i + 1, data))
    # ===== for i: 정렬 종료
    # print(f'정렬 결과: {data}')
    return data


selection_sort_desc(data)


# In[ ]:


if __name__ == '__main__':
    data = [8, 3, 4, 9, 1]
    result = selection_sort_asc(data)
    print(f'정렬 결과: {data}')
    result = selection_sort_desc(data)
    print(f'정렬 결과: {data}')

