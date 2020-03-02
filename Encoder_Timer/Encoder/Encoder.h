#ifndef ENCODER_H
#define ENCODER_H
#include "mbed.h"

void EncoderInit(TIM_Encoder_InitTypeDef * encoder, TIM_HandleTypeDef * timer, TIM_TypeDef * TIMx, uint32_t maxcount, uint32_t encmode);
#endif