all code should be written in the idle shell
show() #shows your diagram on the output tk file
clear_all() #clears your current diagram from the tk file
the runes that are accepted as vars are from the pdf

#prgms that change the diagram
stack(rune1,rune2) #takes 2 rune variables,
                        stacks them on top of each other with equal proportion  eg in a 2x2 box it becomes 2 rune rects on top of each other

stack_frac(1/n,rune1,rune2) #same as stack, BUT stacks rune1 on top and takes up 1/n space
                                    eg
                                    in a box like 000
                                                  000
                                                  000 
                                                  1/3,a,b means aaa
                                                                bbb
                                                                bbb

stackn(n,rune) #stacks n runes on top of each other 

quarter_turn_right(rune) #rotates rune 90 degrees to the right

quarter_turn_left(rune) #rotates rune 90 degrees to the left

eighth_turn_left(rune) #rotates rune 45 degrees to the left

turn_upside_down(rune) #turns rune 180 degrees 

flip_horiz(rune) #flip rune horizontally/turn left_right

flip_vert(rune) #flip rune vertically/turn upside down

beside(rune1,rune2) puts 2 runes side by side, equal proportion

repeat_pattern(n,pattern,rune) #repeats the pattern of a rune for n times, eg repeat_pattern(3,make_cross,rune) means it makes a cross and shows 3 of it
