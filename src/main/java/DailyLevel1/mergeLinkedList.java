package DailyLevel1;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

public class mergeLinkedList {
    public static ListNode mergeTwoLists(ListNode l1, ListNode l2) {

        ListNode result = new ListNode();
        ListNode head = result;
        while(l1!=null && l2!=null){
            if(l1.val<l2.val){
                result.next = l1;
                l1 = l1.next;
            }else{
                result.next = l2;
                l2 = l2.next;
            }

            result = result.next;
        }

        if(l1!=null){
            result.next=l1;
        }else{
            result.next=l2;
        }

        return head.next;
    }

    public static void main(String[] args) {
        ListNode list1 = new ListNode();
        ListNode list2 = new ListNode();
        ListNode head1 = list1;
        ListNode head2 = list2;

//        list1.val = 1;
//        list1.next = new ListNode(2);
//        list1 = list1.next;
//        list1.next = new ListNode(4);
//        list1 = list1.next;

        list2.val = 1;
        list2.next = new ListNode(3);
        list2 = list2.next;
        list2.next = new ListNode(4);
        list2 = list2.next;

        ListNode sortedList = mergeTwoLists(head1,head2);

        sortedList.printList(sortedList);
    }
}
