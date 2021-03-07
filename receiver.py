from common import *
from pickle import TRUE, FALSE
from common import checksumCalc

class receiver:
    
    def isCorrupted(self, packet):
        ''' Checks if a received packet has been corrupted during transmission.
        Return true if computed checksum is different than packet checksum.'''
        print("in receiver isCorrupted....")
        print("packet.checksum = "+str(packet.checksum))
        print("checksumcalc() = "+str(checksumCalc(packet.payload)))
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
    
    def getNextExpectedSeqNum(self):
        '''The expected sequence numbers are 0 or 1'''
        if(self.expectedSeqNum == 1):
            self.expectedSeqNum = 0
            
        else:
            self.expectedSeqNum= 1
            
        return self.expectedSeqNum
            
    
    
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
        
        print("in receiver input()...")
        print("iscorrupted() = "+str(self.isCorrupted(packet)))
        print("isduplicate() = "+str(self.isDuplicate(packet)))
        
        
        if((self.isCorrupted(packet) == TRUE) or (self.isDuplicate(packet) == TRUE)):
            if(self.expectedSeqNum == 1):
                ack_num = 0
            else:
                ack_num = 1
            print("B's ack_num (corrupted or duplicate) = "+str(ack_num))
        
        else:
            ack_num = self.expectedSeqNum           
            print("B's ack_num = "+str(ack_num))  
            self.networkSimulator.deliverData(self.entity, packet)
            
        pkt = Packet(packet.seqNum, ack_num, packet.checksum, packet.payload)
        self.networkSimulator.udtSend(self.entity, pkt)

        self.getNextExpectedSeqNum()

        return
