# 고객 관리 시스템 v0.1
# 데이터 : 이름, 성별, 이메일, 출생년도
# 이름은 문자열
# 성별은 남자는 M, 여자는 F로 
# 이메일은 문자열
# 태어난 연도는 정수

index = -1

def main():
    customer_list = list()
    global index
    # 테스트 데이터 나중에 꼭!!! 지워야 함!
    # test_cust = {'name': '손정현', 'gender': 'M', 'email': 'abc@abc', 'year': 1999}
    # customer_list.append(test_cust)
    # test_cust = {'name': '박정현', 'gender': 'F', 'email': 'bbc@bbc', 'year': 1999}
    # customer_list.append(test_cust)
    # test_cust = {'name': '김정현', 'gender': 'F', 'email': 'ccc@ccc', 'year': 1888}
    # customer_list.append(test_cust)
    while True:
        choice = input('''
            다음 중 하실 일을 골라 주세요.: 
            I - 고객 정보 입력
            U - 고객 정보 수정
            D - 고객 정보 삭제
            P - 이전 고객 정보 조회
            C - 현재 고객 정보 조회
            N - 단음 고객 정보 조회
            Q - 프로그램 종료
        ''').upper()
        if choice == 'I':
            # customer = input_cust()
            customer_list.append(Input.input_cust())
            index = len(customer_list) - 1
        if choice == 'U':
            customer_list = update_cust(customer_list)
        if choice == 'D':
            customer_list = delete.delete_cust(customer_list)
            if index > len(customer_list) - 1:
                index = len(customer_list) - 1
        if choice == 'C':
            if index >= 0:
                print('현재 {}번째 고객 정보 입니다.'.format(index + 1))
                print(customer_list[index])
            else:
                print('입력된 고객 정보가 없습니다.')
        if choice == 'P':
            if index <= 0:
                print('첫 번째 고객 정보 입니다.')
                print(customer_list[0])
            else:
                # index -= 1
                index = index - 1
                print('현재 {}번째 고객 정보 입니다.'.format(index + 1))
                print(customer_list[index])
        if choice == 'N':
            last_index = len(customer_list) - 1
            if index >= last_index:
                print('마지막 번째 고객 정보 입니다.')
                print(customer_list[last_index])
            else:
                # index += 1
                index = index + 1
                print('현재 {}번째 고객 정보 입니다.'.format(index + 1))
                print(customer_list[index])
        if choice == 'Q':
            break
        # print('main : customer_list ', customer_list)
class delete:
    def __init__(self,customer_list,idx):
        self.customer_list = customer_list
        self.idx = idx

    def delete_delete(customer_list, idx):
        customer_list.pop(idx)
        return customer_list

    def delete_cust(customer_list):
        # 테스트 데이터 나중에 꼭!!! 지워야 함!
        # test_cust = {'name': '손정현', 'gender': 'M', 'email': 'abc@abc', 'year': 1999}
        # customer_list.append(test_cust)
        # test_cust = {'name': '박정현', 'gender': 'F', 'email': 'bbc@bbc', 'year': 1999}
        # customer_list.append(test_cust)

        # 고객 정보 검색
        idx = search(customer_list)
        if idx == -1:
            pass
        else:
            customer_list = delete.delete_delete(customer_list, idx)
        # print('삭제 후 데이타 : ', customer_list)
        return customer_list

def search(customer_list):
    email = input('수정 하고 싶은 고객의 이메일 입력 하세요?')
    idx = -1
    for i in range(0, len(customer_list)):
        if customer_list[i]['email'] == email:
            idx=i
            break
    if idx == -1:
        print('등록되지 않은 고객입니다.')
    return idx

def update_update(customer_list, idx):
    while True:
        choice2 = input('''
        다음 중 수정 할 항목을 입력 하세요. 
        name, gender, email, year
        (수정 할 항목이 없으면 "Q"를 입력 하세요)''')

        customer = dict()
        if choice2.lower() == 'year':
            customer = input_year(customer)
        elif choice2.lower() == 'name':
            customer = input_name(customer)
        elif choice2.lower() == 'gender':
            customer = input_gender(customer)
        elif choice2.lower() == 'eamil':
            customer = input_email(customer)
        elif choice2.upper() == 'Q':
            break
        customer_list[idx][choice2] = customer[choice2]
    return customer_list

# 고객 정보 수정
def update_cust(customer_list):
    # customer_list = list()
    # test_cust = {'name': '손정현', 'gender': 'M', 'email': 'abc@abc', 'year': 1999}
    # customer_list.append(test_cust)
    # test_cust = {'name': '박정현', 'gender': 'F', 'email': 'bbc@bbc', 'year': 1999}
    # customer_list.append(test_cust)

    # 고객 정보 검색
    idx = search(customer_list)
    if idx == -1:
        pass
    else:
        # 고객 정보 수정
        customer_list = update_update(customer_list, idx)

    # print('수정 내용 확인 : ', customer_list[idx])
    global index
    index = idx
    print('수정 완료')
    return customer_list

class Input:
    def __init__(self,customer):
        self.customer = customer
# 고객 정보 입력 : 이름
    def input_name(customer):
        # 국내 전용 고객관리 시스템 보편 적인 한글 이름 길이 적용.
        # 특이사항 이름은 5자 이내로 줄여서 등록.
        while True:
            customer['name'] = input('이름을 입력하세요 : ').upper()
            if len(customer['name']) <= 6 :
                break
            else:
                print('이름을 6자 이내로 입력 해 주세요.')
        return customer

    # 고객 정보 입력 : 성별
    def input_gender(customer):
        while True:
            customer['gender'] = input('성별을 M/F로 입력하세요 : ').upper()
            if customer['gender'] in ('M', 'F'):
                break
            else:
                print('성별은 M, F 로 잘 입력 해 주세요.')
        return customer

    # 고객 정보 입력 : 이메일
    def input_email(customer):
        while True:
            customer['email'] = input('이메일 주소를 입력하세요 : ')
            if customer['email'].find('@') != -1:
                break
            else:
                print('이메일 주소 형식을 확인 해 주세요.')
        return customer

    # 고객 정보 입력 : 출생년도
    def input_year(customer):
        while True:
            customer['year'] = input('출생년도를 입력하세요 : ')
            if len(customer['year']) == 4 and customer['year'].isdigit():
                customer['year'] = int(customer['year'])
                break
            else:
                print('출생년도를 정수로 입력하세요.')
        return customer

    # 고객 정보 입력
    def input_cust():
        customer = dict()
        customer = Input.input_name(customer)
        customer = Input.input_gender(customer)
        customer =  Input.input_email(customer)
        customer = Input.input_year(customer)

        # print(customer)
        return customer

if __name__ == '__main__':
    main()