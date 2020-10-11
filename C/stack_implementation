#include <stdio.h>
//declaring global variables
int top=-1; 
int stack[10], value, temp, i;

void main()
{
  int n;
  printf("what you want to do:\n 1.push\n2.pop\n3.exit");
  scanf("%d",&n);

  while(1)
  {                                                    //for continuous insertion or deletion
   switch (n)
   { case 1: {push();
             break;}
    case 2:{pop();
            break;}
    case 3:{
           exit (0);  
           }
    default : printf("invalid"); 
    }
  }
}
 push()
      {
         if (top==9)                                  // for checking overflow condition 
            {   printf("overflow");
                 exit(0);
             }
         else {printf("enter the values");
                scanf("%d ",&stack[top]);
                 top=top+1;
                   
             printf("displaying stack");
               for(i=0;i<=top;i++)                      //display the stack
                printf("%d ",&stack[i]);
               }
       }
       
pop()
{if (top==-1)
   {
     printf("underflow");                               //for checking underflow condition
     exit(0); 
   }
 else {
       temp=stack[top];
        top=top-1;
       printf("displaying stack");                          // display stack
        for(i=0;i<=top;i++)
        printf("%d ",&stack[i]);  }
}
