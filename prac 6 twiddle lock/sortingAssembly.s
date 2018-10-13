/*
R0 address of string used with printf ti output %d
R4 address of numbers to sort
R5 current number to be compared
R6 offset index for outer loop through numbers
R7 offset index for inner loop
R8 current smallest identified value
R9 current offset index of next uncompared value
*/
.global main
main:
  push {ip, lr}
  MOV R6, #0 			@outerloop offset to numbers to be sorted
  MOV R7, #0			@innerloop offers to number to be sorted
  MOV R9, #0			@init value for index to next uncompared value
outerLoop:
  MOV R8, #99			@reset large default for next loop comparison
  MOV R7,R6				@copy outerloop offset to next starting offset for the innerloop
innerLoop:
  LDR R0, =output 		@load addr of output string
  LDR R4, =nums 		@load addr of nums to compare to R4
  LDR R5,[R4,R7] 		@load current num to R5 from R4 with offset R7
  MOV R1,R5 			@move num for output
  BL printf
  CMP R5,R8				@is current < smallest so far
  BLT swapSmallest		@if true, swap smallest to current first position then continue
continue:
  CMP R7,#16    		@ 0 plus 4*4bytes for 5 entries in array
  ADD R7, R7,#4 		@inc offset by 4 bytes
  BLT innerLoop
continueOuterLoop:
  CMP R6, #16			@check if we've looped through all values
  ADD R6, R6, #4
  BLT outerLoop			@if not, branch back to start of outer loop
_exit:
  POP {ip, lr}
resetLoopOffsets:
  MOV R7, #0			@reset loop counter
writeFinalSoredList:	@TODO: this is a near copy of the innner loop - refactor this to function
  LDR R0, =writeSorted 	@load addr of output string
  LDR R4, =nums 		@load addr of nums
  LDR R5,[R4,R7] 		@load current num to R5 from R4 with offset R7
  MOV R1,R5 			@move num for output
  BL printf
  CMP R7,#16    		@ 0 plus 4*4bytes for 5 entries in array
  ADD R7, R7,#4 		@inc offset by 4 bytes
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
nums:
.word 5,2,7,1,8
output:
.asciz "%d\n"
writeSorted:
.asciz "%d\n"
.balign 4
sorted: .skip 20
