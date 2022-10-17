package DailyLevel1;

import java.util.List;

public class ListNode {
      int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }

      void printList(ListNode node){
            System.out.print("["+node.val);
            while(node.next != null){
                  node = node.next;
                 System.out.print(", "+node.val);
           }
            System.out.print("]");
      }
}
