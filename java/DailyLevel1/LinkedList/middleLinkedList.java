package DailyLevel1.LinkedList;

public class middleLinkedList {

    public static void printList(ListNode node){
        System.out.print("\n[");
        while(node != null){
            System.out.print(node.val);
            node = node.next;
            if(node!= null){
                System.out.print(", ");
            }
        }
        System.out.print("]");
    }

    public static ListNode middleNode(ListNode head) {
        ListNode middle = head;
        if (head==null){
            return null;
        }

        head = head.next;
        int count = 1, mid = 1;
        while(head!=null){
            count+=1;
            if(count%2==0){
                if(mid!=(count/2)+1){
                    middle=middle.next;
                    mid+=1;
                }
            }
            else{
                if(mid!=((count+1)/2)){
                    middle=middle.next;
                    mid+=1;
                }
            }
            head = head.next;
        }
        return middle;
    }

    public static void main(String[] args) {
        ListNode list1 = new ListNode();
        ListNode head1 = list1;
        list1.next = new ListNode(1);
        list1.next.next = new ListNode(2);
        list1.next.next.next = new ListNode(4);
        list1.next.next.next.next = new ListNode(6);

        printList(head1.next);
        printList(middleNode(head1.next));
    }
}
