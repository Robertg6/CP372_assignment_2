from common import *

class sender:
    RTT = 20
    
    def isCorrupted (self, packet):
        '''Checks if a received packet (acknowledgement) has been corrupted
        during transmission.
        Return true if computed checksum is different than packet checksum.
        '''
    print("inside sender isCorrupted/n")
        if (packet.checksum != checksumCalc(packet.payload)):
          return True;
        return False;

    def isDuplicate(self, packet):
        '''checks if an acknowledgement packet is duplicate or not
        similar to the corresponding function in receiver side
        '''
        print("inside sender isDuplicate/n")
        if(packet.seqNum == self.expectedSeqNum):
            return FALSE
        
        else:
            return TRUE
 
    def getNextSeqNum(self):
        '''generate the next sequence number to be used.
        '''
        print("inside sender getNextSeqNum/n")
        if(self.expectedSeqNum == 1):
            self.expectedSeqNum = 0
            
        else:
            self.expectedSeqNum = 1
            
        return self.expectedSeqNum

    def __init__(self, entityName, ns):
        self.entity = entityName
        self.networkSimulator = ns
        print("Initializing sender: A: "+str(self.entity))

    def init(self):
        '''initialize the sequence number and the packet in transit.
        Initially there is no packet is transit and it should be set to None
        '''
        print("inside sender init/n")
        sequence_number = 0
        pkt = None
        return

    def timerInterrupt(self):
        '''This function implements what the sender does in case of timer
        interrupt event.
        This function sends the packet again, restarts the time, and sets
        the timeout to be twice the RTT.
        You never call this function. It is called by the simulator.
        '''
        print("inside sender timerInterrupt/n")


        
        return


    def output(self, message):
        '''prepare a packet and send the packet through the network layer
        by calling calling utdSend.
        It also start the timer.
        It must ignore the message if there is one packet in transit
        '''
        print("inside sender output/n")

        
        self.RTT
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
        print("inside sender input/n")
        
        if((self.isCorrupted(packet) == TRUE) or (self.isDuplicate(packet) == TRUE)):
            if(self.expectedSeqNum == 1):
                ack_num = 0
            else:
                ack_num = 1
        
        else:
            if(packet.seqNum == 1):
                ack_num = 1
            else:
                ack_num = 0
            self.RTT*2
                
            self.networkSimulator.deliverData(self.networkSimulator, self.entity, packet)
        return 
