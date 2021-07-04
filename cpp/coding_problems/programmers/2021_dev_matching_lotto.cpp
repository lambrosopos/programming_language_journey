#include <string>
#include <vector>

using namespace std;

int rank_award (int count) {
    if (count == 0) return 6;
    return 7 - count;
}
vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    int actual = 0;
    int possibility = 0;
    
    for (int i=0; i<lottos.size(); i++) {
       	if (lottos[i] == 0) {
            possibility += 1;
            continue;
        } 
        for (int j=0; j<win_nums.size(); j++) {
            if (lottos[i] == win_nums[j]) {
                actual += 1;
                break;
            }
        }
    }
    
    
    vector<int> answer;
    answer.push_back(rank_award(actual + possibility));
    answer.push_back(rank_award(actual));
    return answer;
}
