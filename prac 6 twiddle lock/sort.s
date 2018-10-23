/*
R0 = output variabe
R4 = stuff that needs to be sorted
R5 = current item
R6 =outer loop (ie the first for loop) index
R7 = inner loop (second for loop) index
R8 = current smallest value that will update
R9 = index of next value to compare
*/







.global main @functions like a selection sort with double for loops
main:
  push {ip, lr}
  MOV R6, #0 			@this sets the outer loop offset for numbers to be sorted
  MOV R7, #0			@this sets the inner loop
  MOV R9, #0			@this is the next value to be compared i+1 in a for loop
outerLoop:
  MOV R8, #99			@resets the default comparing value
  MOV R7,R6				@copy the i from outer loop to be used in the inner for loop
innerLoop:
  LDR R0, =output 		@gets the address of the output
  LDR R4, =inputnumbers 		@loads the address of the input
  LDR R5,[R4,R7] 		@load current item taking into account offset r7
  MOV R1,R5 			@move the number to the output address
  BL printf
  CMP R5,R8				@compares the two values to find smallest
  BLT swapSmallest		@if it is smaller, update the output
continue:
  CMP R7,#16    		@ 0 plus 4*4bytes for 5 entries in array
  ADD R7, R7,#4 		@make offset bigger by 4
  BLT innerLoop
continueOuterLoop:
  CMP R6, #16			@check if we've looped through all values
  ADD R6, R6, #4
  BLT outerLoop			@if not, branch back to start of outer loop
_exit:
  POP {ip, lr}
resetLoopOffsets:
  MOV R7, #0			@reset the offsets of the loops
writeFinalSoredList:
  LDR R0, =writeSorted 	@get the address of the output
  LDR R4, =inputnumbers 		@address of the input
  LDR R5,[R4,R7] 		@loads R5 to R4 taking into account R7 as input
  MOV R1,R5 			@move num to the oubut
  BL printf
  CMP R7,#16    		@ 0 plus 4*4bytes for 5 entries in array
  ADD R7, R7,#4 		@increment the offset by 4 bits
  BLT writeFinalSoredList
doExit:
  MOV R1, #0
  MOV R7, #1
  SWI 0
swapSmallest:
  MOV R8,R5				@keep copy of smallest in the current loop
  LDR R10, [R4,R6]		@tmp copy first position to R10
  LDR R11, [R4,R7]		@tmp copy value in position currently being compared
  STR R10, [R4, +R7]	@swap first position value to current position being compared
  STR R11, [R4, +R6]	@swap the current smallest value into the current first position
  BX lr					@return
.data
inputnumbers:
.word 9,7,5,3,1
output:
.asciz "%d\n"
writeSorted:
.asciz "%d\n"
.balign 4
sorted: .skip 20
