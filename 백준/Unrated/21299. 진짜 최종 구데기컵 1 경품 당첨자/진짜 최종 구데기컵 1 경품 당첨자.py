l=[]
match input():
    case'Marathon Edition 우승자':
        pass
    case'Marathon Edition 준우승자 및 ReguIar Edition 준우승자':
        pass
    case'ReguIar Edition 우승자 및 Speedrun Edition 우승자':
        pass
    case'Speedrun Edition 준우승자':
        pass
    case'이 대회에 참가하지 않은 사람 중 2019년 대회 최고 등수':
        pass
    case'모든 에디션에서 총점이 160억점에 가장 가까운 사람':
        pass
    case'홀수와 짝수의 대결 문제의 오류를 발견한 사람':
        pass
    case'4차 산업 혁명을 기계학습 없이 서브태스크 2까지만 푼 사람 중 추첨':
        l+='UPWF 위원회 특별상',
    case'배중률교를 정해가 아닌 방법으로 푼 사람 중 추첨':
        l+='직관주의자상',
    case'Marathon Edition에서 Nonogram QR을 마지막으로 1점 이상 획득한 사람':
        l+='QR 분해 상',
    case'연속합 2147483647 첫 0점자':
        l+='Re: 제로부터 시작하는 다이나믹 프로그래밍 상',
    case'Beginning the Hunt 첫 만점자':
        l+='"Ghudegy Cup looks too intense for me" 상',
    case'대회에 참여하였고 A+B (MC)에 제출하지 않은 사람 중 추첨':
        l+='You Need a Minecraft 상',
l+=[-1]*3
for i in l[:3]:
    print(i)