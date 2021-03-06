#Janelle Tait tait7860
#Robert Goss goss7390
from common import *
from pickle import TRUE, FALSE
from common import checksumCalc

class sender:
    RTT = 20
    
    def isCorrupted (self, packet):
        '''Checks if a received packet (acknowledgement) has been corrupted
        during transmission.
        Return true if computed checksum is different than packet checksum.
        '''
        
        
        if(packet.checksum != checksumCalc(packet.payload)):
            return True;
      
        return False;

    def isDuplicate(self, packet):
        '''checks if an acknowledgement packet is duplicate or not
        similar to the corresponding function in receiver side
        '''
        
        if(packet.seqNum == self.expectedSeqNum):
            return FALSE
        
        else:
            return TRUE
 
    def getNextSeqNum(self):
        '''generate the next sequence number to be used.
        '''
        if(self.sequence_number == 1):
            self.sequence_number = 0
        else:
            self.sequence_number = 1
            
        return self.sequence_number

    def __init__(self, entityName, ns):
        self.entity = entityName
        self.networkSimulator = ns
        print("Initializing sender: A: "+str(self.entity))

    def init(self):
        '''initialize the sequence number and the packet in transit.
        Initially there is no packet is transit and it should be set to None
        '''
        self.sequence_number = 0
        self.pkt = None

        return

    def timerInterrupt(self):
        '''This function implements what the sender does in case of timer
        interrupt event.
        This function sends the packet again, restarts the time, and sets
        the timeout to be twice the RTT.
        You never call this function. It is called by the simulator.
        '''
        #self.RTT = self.RTT*2
        #self.output(self.pkt.payload)
        
        self.networkSimulator.udtSend(self.entity, self.pkt)
        self.networkSimulator.startTimer(self.entity, 2*self.RTT)
        return


    def output(self, message):
        '''prepare a packet and send the packet through the network layer
        by calling calling utdSend.
        It also start the timer.
        It must ignore the message if there is one packet in transit
        '''
        checksum = checksumCalc(message.data)
        
        #pkt = Packet(self.sequence_number, 0, checksum + self.sequence_number, message.data)
        self.pkt = Packet(self.sequence_number, 0, checksum + self.sequence_number, message.data)
        self.networkSimulator.udtSend(self.entity, self.pkt)
        
        self.networkSimulator.startTimer(self.entity, self.RTT)

        #I don't know how to check if there is already a packet in transit (maybe check to see if the timer is already running?)
        #do we need a separate variable to keep track of the timeout? Right now we are just multiplying RTT by 2 but I think thats wrong
        return
 
    
    def input(self, packet):

        '''If the acknowlegement packet isn't corrupted or duplicate, 
        transmission is complete. Therefore, indicate there is no packet
        in transition.
        The timer should be stopped, and sequence number  should be updated.
        In the case of duplicate or corrupt acknowlegement packet, it does 
        not do anything and the packet will be sent again since the
        timer will be expired and timerInterrupt will be called by the simulator.
        '''

    
    
        if((self.isCorrupted(packet) != TRUE) or (self.isDuplicate(packet) != TRUE)):
            self.networkSimulator.stopTimer(self.entity)
            self.SeqNum = self.getNextSeqNum()
            self.pkt = None
            
            
        return

