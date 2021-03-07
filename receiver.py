from common import *
from pickle import TRUE, FALSE
from startSTP.common import checksumCalc

class receiver:
    
    def isCorrupted(self, packet):
        ''' Checks if a received packet has been corrupted during transmission.
        Return true if computed checksum is different than packet checksum.'''
        
        if(packet.checksum != checksumCalc(packet.payload)):
            return TRUE
        
        else:
            return FALSE
   
    def isDuplicate(self, packet):
        '''checks if packet sequence number is the same as expected sequence number'''
        if(packet.seqNum == self.expectedSeqNum):
            return FALSE
        
        else:
            return TRUE
        
        return
    
    def getNextExpectedSeqNum(self):
        '''The expected sequence numbers are 0 or 1'''
        if(self.expectedSeqNum == 1):
            return 0
            
        else:
            return 1
            
    
    
    def __init__(self, entityName, ns):
        self.entity = entityName
        self.networkSimulator = ns
        print("Initializing receiver: B: "+str(self.entity))


    def init(self):
        '''initialize expected sequence number'''
        self.expectedSeqNum = 0;
        return
         

    def input(self, packet):
        '''This method will be called whenever a packet sent 
        from the sender arrives at the receiver. If the received
        packet is corrupted or duplicate, it sends a packet where
        the ack number is the sequence number of the  last correctly
        received packet. Since there is only 0 and 1 sequence numbers,
        you can use the sequence number that is not expected.
        
        If packet is OK (not a duplicate or corrupted), deliver it to the
        application layer and send an acknowledgement to the sender
        '''
        ack_num = 1
        
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
                
            self.networkSimulator.deliverData(self.entity, packet)
            
        pkt = Packet(self, packet.seqNum, ack_num, packet.checksum, packet.payload)
        self.networkSimulator.udtSend(self.networkSimulator, self.entity, pkt)


        return
