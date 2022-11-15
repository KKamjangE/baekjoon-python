# 포인터로 연결 리스트 구현하기

from __future__ import annotations
from typing import Any, Type

class Node:
    """연결 리스트용 노드 클래스"""
    # __init__은 전달받은 data와 next를 해당 필드에 대입 호출할 때 어떤 인수도 생략가능 생략하면 None으로 간주
    def __init__(self, data: Any = None, next: Node = None):
        """초기화"""

        self.data = data # 데이터
        self.next = next # 뒤쪽 포인터
        
class LinkedList:
    """연결 리스트 클래스"""

    def __init__(self) -> None:
        """초기화"""
        self.no = 0 # 노드의 개수
        self.head = None # 머리노드
        self.current = None # 주목노드
        
    def __len__(self) -> int:
        """연결 리스트의 노드 개수를 반환"""
        return self.no
    
    def search(self, data: Any) -> int:
        """data와 값이 같은 노드를 검색"""
        cnt = 0
        ptr = self.head
        while ptr is not None: # 스캔할 노드가 존재하지 않으면 종료
            if ptr.data == data:
                self.current = ptr
                return cnt # 검색 성공 맨 앞에서 몇번째 원소인지 넘겨줌
            cnt += 1
            ptr = ptr.next # ptr을 다음 노드로 대입
        return -1 # 검색 실패
    
    def __contains__(self, data: Any) -> bool:
        """연결 리스트에 data가 포함되어 있는지 확인"""
        return self.search(data) >= 0
    
    def add_first(self, data: Any) -> None:
        """맨 앞에 노드를 삽입"""
        ptr = self.head # 삽입하기 전의 머리노드
        self.head = self.current = Node(data, ptr)
        self.no += 1
        
    def add_last(self, data: Any) -> None:
        """맨 뒤에 노드를 삽입"""
        if self.head is None: # 리스트가 비어있으면
            self.add_first(data) # 맨 앞에 노드를 삽입
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = self.current = Node(data, None) # 꼬리노드의 뒤쪽 포인터 next에 추가
            self.no += 1
            
    def remove_first(self) -> None:
        """머리 노드를 삭제"""
        if self.head is not None: # 리스트가 비어 있지 않다면
            self.head = self.current = self.head.next # 기존 head.next(2번째 노드에 대한 참조)를 head에 대입
        self.no -= 1
        
    def remove_last(self) -> None:
        """꼬리 노드를 삭제"""
        if self.head is not None: # 리스트가 비어있지 않다면
            if self.head.next is None: # 노드가 1개 뿐이라면
                self.remove_first() # 머리 노드를 삭제
            else:
                ptr = self.head # 스캔 중인 노드
                pre = self.head # 스캔 중인 노드의 앞쪽 노드
                
                while ptr.next is not None:
                    pre = ptr
                    ptr = ptr.next
                pre.next = None # pre는 삭제 뒤 꼬리 노드
                self.current = pre # 주목노드를 삭제 뒤 꼬리 노드로 변경
                self.no -= 1
                
    def remove(self, p: Node) -> None:
        """노드 p를 삭제"""
        if self.head is not None: # 리스트가 비어있지 않다면
            if p is self.head: # p가 머리 노드이면
                self.remove_first() # 머리 노드를 삭제
            else:
                ptr = self.head
                
                while ptr.next is not p: # 현재 노드의 next의 값과 비교
                    ptr = ptr.next
                    if ptr is None: # 꼬리 노드의 next가 None이면
                        return # ptr은 리스트에 존재하지 않음
                ptr.next = p.next # 삭제할 노드가 참조하고있는 next노드에 참조를 ptr.next에 대입함
                self.current = ptr
                self.no -= 1
                
    def remove_current_node(self) -> None:
        """주목 노드를 삭제"""
        self.remove(self.current)
        
    def clear(self) -> None:
        """전체 노드를 삭제"""
        while self.head is not None: # 전체가 비어 있을 때까지
            self.remove_first() # 머리 노드를 삭제
        self.current = None
        self.no = 0
        
    def next(self) -> bool:
        """주목 노드를 한 칸 뒤로 이동"""
        if self.current is None or self.current.next is None: # 비어있거나 뒤쪽 노드가 없을때
            return False # 이동할 수 없음
        self.current = self.current.next
        return True
    
    def print_current_node(self) -> None:
        """주목 노드를 출력"""
        if self.current is None: # 비어 있을때
            print('주목 노드가 존재하지 않습니다.')
        else:
            print(self.current.data)
            
    def print(self) -> None:
        """모든 노드를 출력"""
        ptr = self.head # 리스트 순서대로 머리부터
        
        while ptr is not None: # 노드값이 없을때 까지
            print(ptr.data)
            ptr = ptr.next # 뒤로 한칸 이동
            
    def __iter__(self) -> LinkedListIterator:
        """이터레이터를 반환"""
        return LinkedListIterator(self.head)
    
class LinkedListIterator:
    """클래스 LinkedList의 이터레이터용 클래스"""
    
    def __init__(self, head: Node): # 받은 노드를 머리 노드로
        self.current = head
        
    def __iter__(self) -> LinkedListIterator: # 이터레이터 반환
        return self
    
    def __next__(self) -> Any:
        if self.current is None: # 빈칸이 아니면
            raise StopIteration # 꺼낼 원소가 없으면 예외 처리
        else:
            data = self.current.data # 현재 위치한 원소 꺼냄
            self.current = self.current.next # 뒤의 원소로 이동
            return data