package DailyLevel1.LinkedList;

public class reverseLinkedList {
    public static ListNode reverseList(ListNode head) {
        ListNode previous = new ListNode();
        ListNode current = head;
        ListNode next = new ListNode();

        if(head==null){
            return null;
        }

        while (current!=null){
            next = current.next;
            current.next = previous;
            previous = current;
            current = next;
        }
        head.next = null;
        head = previous;
        return head;
    }

    public static void printList(ListNode node){
        System.out.print("[");
        while(node != null){
            System.out.print(node.val);
            node = node.next;
            if(node!= null){
                System.out.print(", ");
            }
        }
        System.out.print("]");
    }

    public static void main(String[] args) {
        ListNode list1 = new ListNode();
        ListNode head1 = list1;
        list1.next = new ListNode(1);
        list1 = list1.next;
        list1.next = new ListNode(2);
        list1 = list1.next;
        list1.next = new ListNode(4);
        list1 = list1.next;
        list1.next = new ListNode(6);
        list1 = list1.next;

        printList(reverseList(head1.next));
    }
}
