#include <msp430.h>
// Global Variables
#define RED BIT5
#define GREEN BIT7
#define BLUE BIT6

unsigned int adc[3] = {0};  // This will hold the x,y and z axis values
unsigned int X_Axis = 0;
float dimled;
unsigned int Y_Axis = 0;
unsigned int Z_Axis = 0;

float i,X,Y,L,R,B,G;
double z;
int Xmax=1024, Xmin=650, Ymax=1024, Ymin=650, Zmax=560, Zmin=360,TR=0, TB=0, TG=0, Tr=0, Tb=0, Tg=0;
//Function Prototypes
void ConfigureAdc(void);        // Setup watchdog timer, clockc, ADC ports
void getanalogvalues(void); // This function reads the ADC and stores the x, y and z values
void setRedColor(void);
void setBlueColor(void);
void setGreenColor(void);
void setPurpleColor(void);
void setTealColor(void);
void setYellowColor(void);
void fadeLED(int Blue, int Red, int Green);
void fadeLEDG(int valuePWM);
void setBlueOFF();
void setRedOFF();
void setGreenOFF();

int main(void)
{
    WDTCTL = WDT_MDLY_8; // Run for 8 ms - reset after 8ms at (_enable_interrupts)
    IE1 |= WDTIE;
    _enable_interrupts();  // interrupt reset watchdogtimer and sets LED's On and RESET Counters

    P1DIR = 0;

    P1DIR |= ( BLUE | RED | GREEN );                // set bit  0, 1 , 2  as outputs
    P1OUT = 0;

    ConfigureAdc();
    __delay_cycles(250);
    getanalogvalues();
    __delay_cycles(250);


    for(;;){

    	getanalogvalues();
    	R=(Y_Axis-Ymin)/Y;
        TR=8*R;
        G=(Z_Axis-Zmin)/L;
        TG=8*G;
        B=(X_Axis-Xmin)/X;
        TB=8*B;
        TACTL= TASSEL_2|ID_3|MC_1|TAIE; // "TACTL: Select" = "SM clock"  "Divides by 8" "Up-mode" "interrupt"
        TACCR0=1250;                     // "125000 / 125 = 10ms w/ Cycles"
        _enable_interrupts();


        //fadeLED(TB,TR,TG);

        __delay_cycles(25000);

    }
 }

void ConfigureAdc(void)
{
      ADC10CTL1 = INCH_2 + CONSEQ_1;            // A2/A1/A0, single sequence
      ADC10CTL0 = ADC10SHT_2 + MSC + ADC10ON + ADC10IE;
      ADC10DTC1 = 0x03;                         // 3 conversions
      ADC10AE0 |= 0x03;                         // Disable digital I/O on P1.0 to P1.2
}
void getanalogvalues(void)
{
    ADC10CTL0 &= ~ENC;
    while (ADC10CTL1 & BUSY);               // Wait if ADC10 core is active
    ADC10SA = (unsigned int)adc;            // Copies data in ADC10SA to unsigned int adc array
    ADC10CTL0 |= ENC + ADC10SC;             // Sampling and conversion start

    Y_Axis = adc[0];                        // adc array 0 copied to the variable X_Axis
    X_Axis = adc[1];                        // adc array 1 copied to the variable Y_Axis
    Z_Axis = adc[2];                        // adc array 2 copied to the variable Z_Axis
    __bis_SR_register(CPUOFF + GIE);        // LPM0, ADC10_ISR will force exit

    Y=Ymax-Ymin;
    L=Zmax-Zmin;
    X=Xmax-Xmin;
}

void fadeLED(int Blue, int Red, int Green)
{
}

#pragma vector=ADC10_VECTOR
__interrupt void ADC10_ISR(void)
{
  __bic_SR_register_on_exit(CPUOFF);        // Clear CPUOFF bit from 0(SR)
}
#pragma vector=TIMER0_A1_VECTOR
__interrupt void Timer_A(void)
{
    switch(TAIV){
    case 0x02: break;
    case 0x04: break;
    case 0x0A:                                 // (Compare counter to Timer){ assign: reest }
        if(Tr>=TR)
        {
            P1OUT |= RED;

        }
        if(Tb>=TB)
        {
            P1OUT |= BLUE;

        }
        if(Tg>=TG)
        {
            P1OUT |= GREEN;

        }
        Tr++;
        Tb++;
        Tg++;
  break;
        }
  //  return;
}
#pragma vector= WDT_VECTOR
__interrupt void WDT(void)
{
    P1OUT &= ~BLUE;
    P1OUT &= ~RED;
    P1OUT &= ~GREEN;
    Tr=0;
    Tb=0;
    Tg=0;
    getanalogvalues();
    R=(Y_Axis-Ymin)/Y;
    TR=8*R;
    G=(Z_Axis-Zmin)/L;
    TG=8*G;
    B=(X_Axis-Xmin)/X;
    TB=8*B;
}

Attachments area
