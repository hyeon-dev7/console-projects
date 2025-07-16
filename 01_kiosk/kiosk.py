# 25.05.26 ~ 30
# 파이썬 콘솔 키오스크

mc_morning = { "1.베이컨토마토맥머핀": [4500, 3000], "2.베이컨에그맥머핀" : [4300, 2800],
               "3.소시지에그맥머핀" : [4000, 2500], "4.에그맥머핀" : [3800, 2300] }

burger = { "1.빅맥" : [6500, 5000, "비프"], # [세트 가격, 단품, 분류]
           "2.맥스파이시 상하이 버거" : [6500, 5000, "치킨"],
           "3.1955 버거" : [6800, 5300, "비프"],
           "4.더블 불고기 버거" : [6300, 4800, "불고기"],
           "5.베이컨 토마토 디럭스 버거" : [6800, 5300, "비프"], # 1~5번 맥런치 가능
           "6.쿼터파운더 치즈 버거" : [7000,5500,"비프"], "7.슈슈버거" : [6000, 4500, "씨푸드"],
           "8.치즈버거" : [5000, 3500, "비프"], "9.햄버거" : [4500, 3000, "비프"]  }

side = { "1.맥윙" :2400, "2.감자튀김" : 2000, "3.맥너겟": 2000, "4.코울슬로" :2300, "5.치즈스틱": 2600 }

drink = { "1.아이스아메리카노" : 2000, "2.아메리카노" : 2000, "3.아이스카페라떼" : 3000, "4.카페라떼" :3000,
          "5.콜라" : 2000, "6.제로콜라" : 2000, "7.스프라이트" : 2000, "8.환타" : 2000, "9.쉐이크" : 2500 }


import datetime
now = datetime.datetime.now()

cart = {}


def time_check(now) -> int:
    if 4 <= now.hour <= 13:
        if now.hour < 10 or (now.hour == 10 and now.minute <= 30):
            return 1
        else : return 2
    else : return 3


def choose_category() -> str:
    while True :
        if time_check(now) == 1:
            category = input("\n1.맥모닝  2.사이드  3.음료  4.이전화면  0.처음으로 > ")
        elif time_check(now) == 2:
            category = input("\n1.맥런치  2.사이드  3.음료  4.이전화면  0.처음으로 > ")
        else:
            category = input("\n1.버거  2.사이드  3.음료  4.이전화면  0.처음으로 > ")
        if not ("0" <= category <= "4") : continue
        return category


def choose_menu(category) :
    print()
    select ={}
    user_menu =""

    if category == "1":
        if time_check(now) == 1 :
            while user_menu != "0" and user_menu != "10" :
                for i in mc_morning:
                    print("{} : 단품 {}원".format(i, mc_morning[i][1]))
                user_menu = input("메뉴 번호를 선택해 주세요 (10.이전화면  0.처음으로) > ")

                for i in mc_morning:
                    if i[0] == user_menu:
                        set_menu = int(input("\n{} 선택하셨습니다. \n1.세트 {}원 2.단품{}원 (10.이전화면  0.처음으로) > ".format(i[2:], mc_morning[i][0], mc_morning[i][1])))
                        if set_menu == 10: break
                        elif set_menu == 0: main()
                        select[i] = [mc_morning[i][set_menu-1], 1]
                        if set_menu == 1:
                            # select = set_detail(select, i)
                            return set_detail(select, i)
                        return select

        elif time_check(now) == 2 :
            while user_menu != "0" and user_menu != "10" :
                for i, e in enumerate(burger):
                    if i > 4:
                        break
                    print("{} : 단품 {}원, {}".format(e, burger[e][1] - 500, burger[e][2]))
                user_menu = input("메뉴 번호를 선택해 주세요 (10.이전화면  0.처음으로) > ")
                for i in burger:
                    if i[0] == user_menu:
                        set_menu = int(input(
                            "\n{} 선택하셨습니다. \n1.세트 {}원 2.단품{}원 (10.이전화면  0.처음으로) > ".format(i[2:], burger[i][0] - 500, burger[i][1] - 500)))
                        if set_menu == 10: break
                        elif set_menu == 0: main()

                        select[i] = [burger[i][set_menu - 1] - 500, 1]
                        if set_menu == 1:
                            return set_detail(select, i)
                        return select

        else :
            while user_menu != "0" and user_menu != "10":
                for i in burger :
                    print("{} : 단품 {}원, {}".format(i, burger[i][1], burger[i][2]))
                user_menu = input("메뉴 번호를 선택해 주세요 (10.이전화면  0.처음으로) > ")
                for i in burger:
                    if i[0] == user_menu:
                        set_menu = int(input("\n{} 선택하셨습니다. \n1.세트{}원 2.단품{}원 (10.이전화면  0.처음으로) > ".format(i[2:], burger[i][0], burger[i][1])))
                        if set_menu == 10: break
                        elif set_menu == 0: main()

                        select[i] = [burger[i][set_menu - 1],1]
                        if set_menu == 1:
                            return set_detail(select, i)
                        return  select

    elif category == "2":
        while user_menu != "0" and user_menu != "10" :
            for i in side:
                print("{} : {}원".format(i, side[i]))
            user_menu = input("메뉴 번호를 선택해 주세요 (10.이전화면  0.처음으로) > ")
            for i in side:
                if i[0] == user_menu:
                    select[i] = [side[i], 1]
                    return select
    else:
        while user_menu != "0" and user_menu != "10" :
            for i in drink:
                print("{} : {}원".format(i, drink[i]))
            user_menu = input("메뉴 번호를 선택해 주세요 (10.이전화면  0.처음으로) > ")
            for i in drink:
                if i[0] == user_menu:
                    select[i] = [drink[i], 1]
                    return select

    if user_menu == "10":
        return choose_menu(choose_category())
    elif user_menu == "0": main()
    return select


def set_detail(select, key) -> dict:
    while True :
        set_large = ""
        diff1 = 0
        l = input("\n라지 사이즈로 변경하시겠습니까?(+700원) 1.예 2.아니요  (10.이전화면  0.처음으로) > ")
        if l == "10" : choose_menu("1")
        elif l=="0" : return
        elif l == "1":
            # select[key] += 700 # 이렇게 하니까 뒤로가기 할 때마다 가격이 더해짐
            diff1=700
            set_large = "라지"
        elif l=="2":
            set_large = "기본"
        else : continue

        while True:  # change side
            diff2, set_side = set_details(side) # choose_menu 재사용하고 싶었는데 뒤로가기 문제생김
            if diff2 == 10: break

            while True:  # change drink
                diff3, set_drink = set_details(drink)
                if diff3 == 10: break
                select = {key+" "+set_large+" "+set_side[2:]+" "+set_drink[2:]: [select[key][0] + diff1 + diff2 + diff3, 1]}
                return select


def set_details(dict):
    print()
    for i in dict:
        print("{} : {}원".format(i, dict[i]))
    s = input("번호를 선택해 주세요(기본:감튀,콜라)   (10.이전화면  0.처음으로) > ")
    tmp = {}
    set_ = ""
    diff = 0
    if s == "10":
        return 10, 10
    elif s == "0": main()
    for i in dict:
        if i[0] == s:
            tmp[i] = dict[i]
        for j in tmp:
            if tmp[j] != 2000:
                diff = tmp[j] - 2000
            set_ = j
    return diff, set_


def add_to_cart(select) -> dict:
    for i in select:
        if i in cart:
            cart[i][1] += 1
        else :
            cart[i] = select[i]
    return cart


def change_cart(cart) :
    del_dict={}
    for i in cart:
        while True:
            print(i[2:], "{}".format(cart[i]))
            n = int(input("수량을 입력해 주세요 (0:삭제) > "))
            if n >= 1:
                cart[i][-1] = n
                break
            if n == 0:
                del_dict[i] = cart[i]
                break
            else:
                print("입력 오류입니다.")
                continue

    if len(del_dict)>0 :
        for i in del_dict :
            if i in cart:
                if del_dict[i] == cart[i]:
                    del cart[i]
    if len(cart)!=0 :
        return print("수량이 변경되었습니다. {}".format(cart))
    else : return print("장바구니가 비어 있습니다.. ")


def is_paid() :
    while True:
        pay = input("\n결제 수단을 선택해주세요 1.카드 2.상품권  10.이전 > ")
        if pay == "10": return False

        while True :
            if pay == "1":
                card = input("\n카드를 투입구에 꽂아주세요 (1선택) (10.이전 0.처음으로) > ")
                if card == "1": return True
                elif card =="10": break
                elif card =="0": main()
                else : print("시간 초과")

            elif pay == "2":
                payment = input("\n상품권 번호 6자리를 입력해 주세요 (10.이전 0.처음으로) > ")
                if len(payment) == 6 : return True
                elif payment == "10" : break
                elif payment == "0" : main()
                else:
                    print("유효하지 않은 번호입니다.")
                    continue


def print_order(cart, to_go) :
    print("결제가 완료되었습니다.\n\n주문서")
    print(to_go)
    total = 0
    for i in cart :
        total += cart[i][0] * cart[i][-1]
        print("{} (단가 :{} 수량 : {})".format(i[2:], cart[i][0], cart[i][1]))
    print("총 결제 금액 : {}원\n\n".format(total))
    cart.clear()


def main () :
    while True :
        user_start = input("주문 시작 ㅡ 1번을 눌러주세요 > ")
        if user_start == "1":
            while True:
                to_go = input("1.매장  2.포장  0.처음으로 > ")
                if to_go == "0": break
                elif to_go != "1" and to_go != "2": continue
                else :
                    while True:
                        category = choose_category()
                        if category == "0": main()
                        elif category == "4": break
                        else : select = choose_menu(category)
                        if to_go == "1":
                            to_go= "매장"
                        else : to_go = "포장"
                        # print(to_go,":",select)

                        while True :
                            add_cart = input("\n선택하신 {} \n1.장바구니담기  0.종료(처음으로) > ".format(select))
                            # 2.이전으로 도 만들고 싶었으나 구현 실패.. 어디서 왔는지를 모르는데 어떻게 뒤로 가지..?
                            if add_cart == "1":
                                add_to_cart(select)
                                break
                            elif add_cart == "0": main()
                            else :
                                print("입력 오류입니다.")
                                continue
                        select.clear()

                        while True :
                            user_input = input("\n1.장바구니확인  2.메뉴추가   0.종료(처음으로) > ")
                            if user_input == "2":
                                break
                            elif user_input == "0": main()
                            elif user_input == "1":
                                if len(cart)==0 :
                                    print("장바구니가 비어 있습니다.. ")
                                    continue

                                for i in cart:
                                    print(i[2:], "{}".format(cart[i]))

                                while True:
                                    order = input("\n주문하시겠습니까? 1.예 2.수량변경 3.장바구니확인/메뉴추가  0.종료(처음으로) > ")
                                    if not ("0"<=order<="3"):
                                        print("입력 오류입니다.")
                                    elif order == "3" : break
                                    elif order == "0" : main()
                                    else :
                                        if len(cart) != 0:
                                            if order == "1":
                                                while True :
                                                    if is_paid():
                                                        print_order(cart, to_go)
                                                        main()
                                                    else: break

                                            elif order == "2":
                                               change_cart(cart)
                                        else : print("장바구니가 비어 있습니다.. ")
                            else : continue

main()
