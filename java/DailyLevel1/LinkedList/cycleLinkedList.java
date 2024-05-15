package DailyLevel1.LinkedList;

import java.util.ArrayList;
import java.util.List;

public class cycleLinkedList {

    public static void printPOS(ListNode node, ListNode cyclenode){
        if(cyclenode==null) System.out.println(-1);
        int pos = 0;
        while(node!=cyclenode){
            pos++;
            node = node.next;
        }
        System.out.println(pos);
    }

    public static ListNode detectCycle(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) break;
        }
        if (fast == null || fast.next == null) return null;
        while (head != slow) {
            head = head.next;
            slow = slow.next;
        }
        return head;
    }

    public static void main(String[] args) {
        ListNode list1 = new ListNode();
        ListNode head1 = list1;
        list1.next = new ListNode(1);
        list1.next.next = new ListNode(2);
        list1.next.next.next = new ListNode(4);
        list1.next.next.next.next = new ListNode(6);
        list1.next.next.next.next.next = list1.next.next.next;

        printPOS(head1.next,detectCycle(head1.next));
    }
}
