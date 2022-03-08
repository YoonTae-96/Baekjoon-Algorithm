while True:
    sent = input()
    if sent == '.':
        break
    st = []

    for i in sent:
        if i not in '()[]':
            continue
        if i == '(' or i == '[':
            st.append(i)
        elif (i == ')' and st and st[-1] == '(') or (i == ']' and st and st[-1] == '['):
            st.pop()
        else:
            st.append(0)
            break

    print('NO' if st else 'YES')