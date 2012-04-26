################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../ADC.c \
../Commands.c \
../ID.c \
../InitializeSystem.c \
../MotorControl.c \
../PinChange.c \
../Servo.c \
../StepperMotor.c \
../Timer2.c \
../main.c \
../serial.c 

OBJS += \
./ADC.o \
./Commands.o \
./ID.o \
./InitializeSystem.o \
./MotorControl.o \
./PinChange.o \
./Servo.o \
./StepperMotor.o \
./Timer2.o \
./main.o \
./serial.o 

C_DEPS += \
./ADC.d \
./Commands.d \
./ID.d \
./InitializeSystem.d \
./MotorControl.d \
./PinChange.d \
./Servo.d \
./StepperMotor.d \
./Timer2.d \
./main.d \
./serial.d 


# Each subdirectory must supply rules for building sources it contributes
%.o: ../%.c
	@echo 'Building file: $<'
	@echo 'Invoking: AVR Compiler'
	avr-gcc -Wall -Os -fpack-struct -fshort-enums -funsigned-char -funsigned-bitfields -mmcu=atmega644p -DF_CPU=8000000UL -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -c -o"$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


