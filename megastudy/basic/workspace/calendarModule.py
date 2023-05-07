#!/usr/bin/env python
# coding: utf-8

# 인수로 연도를 넘겨받아 윤년, 평년을 판단해 윤년이면 True, 평년이면 False를 리턴하는 isLeapYear(year) 함수를 만든다.

# In[9]:


def isLeapYear(year):
    # 연도가 4로 나눠떨어지고 100으로 나눠떨어지지 않거나, 400으로 나눠떨어지면 윤년, 그렇지 않으면 평년
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


# 인수로 연, 월을 넘겨받아 그 달의 마지막 날짜를 리턴하는 lastDay(year, month) 함수를 만든다.

# In[10]:


def lastDay(year, month):
    # 각 달의 마지막 날짜를 기억하는 리스트를 만든다.
    m = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 인수로 넘겨받은 연도에 해당하는 2월의 마지막 날짜를 확정한다.
    m[1] = 29 if isLeapYear(year) else 28
    # 마지막 날짜를 리턴시킨다.
    return m[month - 1]


# 인수로 연, 월, 일을 넘겨받아 1년 1월 1일부터 지나온 날짜의 합계를 리턴하는 totalDay(year, month, day) 함수를 만든다.

# In[4]:


def totalDay(year, month, day):
    # 인수로 넘어온 연도가 다 지나가지 않았으므로 1년 1월 1일부터 전년도 12월 31일까지 지난 날짜를 계산한다.
    s = (year - 1) * 365 + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400
    # 전년도 12월 31일까지 지난 날짜에 전달까지 지난 날짜를 더한다.
    for i in range(1, month):
        s += lastDay(year, i)
    # 전달까지 자난 날짜에 일을 더해 리턴시킨다.
    return s + day


# 인수로 연, 월, 일을 넘겨받아 요일을 계산해서 숫자로 리턴하는 weekDay(year, month, day) 함수를 만든다.
# 일요일(0), 월요일(1), ..., 토요일(6)

# In[5]:


def weekDay(year, month, day):
    return totalDay(year, month, day) % 7


# In[13]:


# 파이썬 파일 1개만 사용할 때는 if __name__ == '__main__': 를 사용하든 말든 아무런 차이가 없다.
# 현재 파이썬 파일이 다른 파이썬 파일에서 모듈로 import 된다면 if __name__ == '__main__': 블럭 내부의 코드가 실행되지 않는다.
if __name__ == '__main__':
    print(isLeapYear(2022))
    print(lastDay(2022, 11))
    print(totalDay(2022, 11, 18))


# In[ ]:




