import java.util.Arrays;
import java.util.Scanner;

public class Solution{
  static long[][] comb = new long[2501][2501];
  public static void main(String[] args) throws Exception{
    Scanner sc = new Scanner(System.in);
    int T;
    T = sc.nextInt();

    for(int test_case = 1; test_case <= T; test_case++){  
      int R = sc.nextInt();
      int C = sc.nextInt();
      int K = sc.nextInt();
      long mod = 1000000007;
      long result = 0;
    
      // case 0 : ���γ� ���ΰ� 1�� ���
      // case 0 : ���γ� ���ΰ� 1�� ���
      if(R == 1 || C == 1){
        if(K == 1 && R == C){
          result = 1;
        
        }
        else if(K == 1){
          result = 0;
        }
        else{
          result = combination(R * C - 2, K - 2) % mod;
        
        }
      }
      else{
        
        // case 1 : �밢�� 4
        long case_1 = combination(R * C - 4, K - 4) % mod;
        // case 2 : �밢�� 3
        long case_2 = 4 * combination(R * C - 4, K - 3) % mod;
        // case 3 : �밢�� 2, �ݴ��� ��ġ
        long case_3 = 2 * combination(R * C - 4, K - 2) % mod;
        // case 4 : �밢�� 2, �����ʿ� ��ġ
        long case_4 = 2 * (2 * combination(R * C - 4, K - 2) % mod - combination(R * C - 2 - R, K - 2) % mod - combination(R * C - 2 - C, K - 2) % mod) % mod;
        // case 5 : �밢�� 1
        long case_5 = 4 * (combination(R * C - 4, K - 1) % mod - combination(R * C - 2 - R, K - 1) % mod - combination(R * C - 2 - C, K - 1) % mod +  combination(R * C - R - C, K - 1) % mod) % mod;
        // case 6 : �밢�� 0 - �� ���̽����� ����� ��¥ ���� �Ұ��� ����...
        long case_6 = (combination(R * C - 4, K) % mod - 2 * (combination(R * C - R - 2, K) % mod + combination(R * C - C - 2, K) % mod) % mod + 4 * combination(R * C - R - C, K) % mod - 2 *(combination(R * C - 2 * C - R + 2, K) % mod + combination(R * C - 2 * R - C + 2, K) % mod) % mod + combination(R * C - 2 * C, K) % mod + combination(R * C - 2 * R, K) % mod + combination(R * C - 2 * C - 2 * R + 4, K) % mod) % mod;

        result = (case_1 + case_2 + case_3 + case_4 + case_5 + case_6) % mod;
        // System.out.println(case_1+" "+case_2+" "+case_3+" "+case_4+" "+case_5+" "+case_6);

      }
      System.out.println("#"+test_case+" "+result);
    }
  }
  // �Ź� �� �� ���� ���չ迭�� ������ ���� 50 X 50 �� ���� �ĵ��� �̸� ���س��´ٸ�?

  public static long combination(int a, int b){
    // ������ �ö󰡸� ��ġ�� Dynamic programming �ϸ� �Ǵ� ����...
    
    
    if(a < b || a < 0 || b < 0){
      return 0;
    }
    else if(a == 0){
      return 1;
    }
    long result = 0;
    int mod = 1000000007;

    
    
    for(int i = 2;i <= a;i++){
      for(int j = 0;j <= i;j++){
        if(comb[i][j] == 0){
          if(i == j || j == 0){
            comb[i][j] = 1;
          }
          else if(j == 1 || i - j == 1){
            comb[i][j] = i;
          }
          else{
            comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % mod;
          }
        }
      }
    }
    
    return comb[a][b];

    
  }
}
