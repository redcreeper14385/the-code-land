/*
CHAIN MATRIX MULTIPLICATION BY SAURABH VERMA
OUTPUT SAMPLE
--------------
Enter number of matrices: 6
Enter dimensions
Enter d0 : 4
Enter d1 : 6
Enter d2 : 7
Enter d3 : 1
Enter d4 : 2
Enter d5 : 5
Enter d6 : 9
Minimum number of multiplications is 157
(A*(B*C))*((D*E)*F)
*/


#include<stdio.h>
#include<string.h>
#define MAX 100
int matrix[MAX][MAX];
void insertAtPos(char list[], int val, char pos)
{
    char temp[MAX] = {};
    int i, a=0, b=0, c=0, index;
    for(i=0;i<MAX;i++)
        if(list[i]=='A'+val-1)
        {
            index = i+1;
            break;
        }
    if(pos=='L')
    {
        do{
            if(index-1==b)
                temp[b++] = '(';
            else
                temp[b++] = list[a++];
        }   
        while(list[a]!=0);
    }
    else
    {
        do{
            if(index==b)
                temp[b++] = ')';
            else
                temp[b++] = list[a++];
        }   
        while(list[a]!=0);
    }
    while(temp[c]!=0)
        list[c]=temp[c++];
}
void divideNcon(char r[], int low, int high)
{
    if(high-low>1)
    {
        int select = matrix[low][high];
        if(low!=select)
        {
            insertAtPos(r,low,'L');
            insertAtPos(r,select,'R');
        }
        if(select+1!=high)
        {
            insertAtPos(r,select+1,'L');
            insertAtPos(r,high,'R');
        }
        divideNcon(r,low,select);
        divideNcon(r,select+1,high);
    }
}
int main()
{
    int i, j, k, L, q, n, c=0, m[MAX][MAX];
    char result[MAX] = {};
    printf("Enter number of matrices: ");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        result[c++] = 'A'+i;
        if(i<n-1)
            result[c++] = '*';
    }
    result[c] = ' '; //do not remove this line!
    int arr[++n];
    printf("Enter dimensions \n");
    for(i=0;i<n;i++)
    {
        printf("Enter d%d : ",i);
        scanf("%d",&arr[i]);
    }
    int num = sizeof(arr)/sizeof(arr[0]);
    for (L=2; L<num; L++)
        for (i=1; i<num-L+1; i++)
        {
            j = i+L-1;
            m[i][j] = 9999;
            for (k=i; k<=j-1; k++)
            {
                q = m[i][k] + m[k+1][j] + arr[i-1]*arr[k]*arr[j];
                if (q < m[i][j])
                {
                    m[i][j] = q;
                    matrix[i][j] = k;
                }
            }
        }
    printf("\nMinimum number of multiplications is %d \n", m[1][num-1]);
    divideNcon(result,1,n-1);
    printf("%s\n",result);
    return 0;
}