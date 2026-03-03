# 마이쮸 문제 바로 간다
def Mychew(total_count):

    queue = []
    queue.append((1,1))

    next_person = 2
    # 마이쮸 남아있으면 계속 나눠줘 떨어질때까지
    while total_count > 0:
        # 큐에서 뽑아서 첫번째는 사람 두번째는 받는 마이쭈개수임
        person, cnt = queue.pop(0)
        # 만약 남은 마이쮸개수가 그사람이 받아야하는 마이쮸의 개수보다 작거나 같으면 그사람이 마이쮸를 받는 마지막사람임
        if total_count - cnt <= 0:
            return person

        # 마이쮸 나눠줘야함
        total_count -= cnt

        # 마이쮸받고나면 받은 사람이 다시 줄서기시작함
        queue.append((person, cnt + 1))

        # 그리고 그걸본 다른 사람들이 호다닥 따라서 줄서기 시작함
        queue.append((next_person, 1))

# 이러면 마지막으로 사탕 받은사람이 몇번사람인지 계산 결과 출력할수 있음.
print(Mychew(20))