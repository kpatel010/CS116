def top(n, i):
  '''
  Prints 3 segments of special characters, where the first segments consists of 
  backsplashes, the second consistes of vertical lines, 
  and the last segment consistes of fronsplashs. The spacing between these
  segments is dependant on i and n
  
  Effects: 
    Prints to the screen
  
  top: Nat Nat -> None 
  Requires:
    n > 0 
    i = 0 
  
  Examples:
    Calling top(1, 0) => None
    prints the following \\|||||//
      
    Calling top(3,0) => None
    prints the following \\  |||||  //
                          \\ ||||| //
                           \\|||||//
  '''
  if n == i:
    return ''
  else:
    print((i * ' ') + '\\\\' + ((n - i - 1) * ' ') + '|||||' + \
    ((n - i - 1) * ' ')  + '//' + ((i) * ' '))
    (top(n, i + 1))


def middle(n):
  '''
  Prints '||o||' and the amount of space before and after string is dependant 
  on n
  
  Effects: 
    Prints to screen 
  
  middle: Nat -> None 
  Requries:
    n > 0 
    
  Examples:
    Calling middle(5) => None
    prints the following       ||o||       
    There are 6 spaaces before and after image
    
    Calling middle(10) => None 
    prints the following            ||o||           
    There are 11 spaces before and after image 
    '''
  print(((n + 1) * ' ') + '||o||' + ((n + 1) * ' '))
  
  
def bottom(n, i):
  '''
  Prints 3 segments of special characters, where the first segments consists of 
  backsplashes, the second consistes of vertical lines, 
  and the last segment consistes of fronsplashs. The spacing between these
  segments is dependant on i and n
  
  Effects: 
    Prints to the screen
  
  top: Nat Nat -> None 
  Requires:
    n > 0 
    i = 0 
  
  Examples:
    Calling bottom(2, 0) => None
    prints the following  //|||||\\
                         // ||||| \\
    
      
    Calling bottom(6,0) => None
    prints the following      //|||||\\     
                             // ||||| \\    
                            //  |||||  \\   
                           //   |||||   \\  
                          //    |||||    \\ 
                         //     |||||     \\

  '''
  if n == i:
    return 
  else:
    print(((n - i - 1) * ' ')  + '//' + ((i) * ' ') + '|||||' + \
    (i * ' ') + '\\\\' + ((n - i - 1) * ' ') )
    (bottom(n, i + 1))


def x_wing(n):
  '''
  Prints an image of an X-wing, which consistes of 3 components, the top, the
  middle and the bottom. The top component is comprised of a series of
  backsplashes, vertical lines and frontsplashes. The middle component is 
  comprised of vertical lines and an 'o' in the middle. The bottom component
  is comprised of a series of backsplashes, vertical lines and frontsplashes. 
  All components are dependant on n
  
  Effects: 
    Prints on screen 
  
  x_wing: Nat => None
  Requires:
    n > 0
    
  Examples:
  Calling x_wing(1) => None
  The following gets printed  \\|||||//
                                ||o||  
                              //|||||\\
  
  Calling x_wing(3) => None 
  prints the following  \\  |||||  //
                         \\ ||||| // 
                          \\|||||//  
                            ||o||    
                          //|||||\\ 
                         // ||||| \\ 
                        //  |||||  \\

  
  '''
  top(n, 0)
  middle(n)
  bottom(n, 0)