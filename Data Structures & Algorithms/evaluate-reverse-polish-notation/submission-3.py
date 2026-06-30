class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for i in tokens:
            if i=="+":
                st.append(st.pop()+st.pop())
            elif i=="-":
                st.append(-st.pop()+st.pop())
            elif i=="*":
                st.append(st.pop()*st.pop())
            elif i=="/":
                a=st.pop()
                st.append(int(st.pop()/a))
            else:
                st.append(int(i))
        return st[-1]