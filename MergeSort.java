class MergeSort {
	public void merge(int arr[], int l, int m, int r) {
		// find sizes for temp arrays
		int n1 = m - l  + 1;
		int n2 = r - m;

		// create temp arrays
		int L[] = new int[n1];
		int R[] = new int[n2];

		// store data in temp arrays
		for (int i = 0; i < n1; i++)
			L[i] = arr[l + i];

		for (int i = 0; i < n2; i++)
			R[i] = arr[m + 1 + i];

		int i = 0, j = 0; // initial index of sub-arrays
		int k = l; // initial index of merged array

		/* merge temp arrays */
		while (i < n1 && j < n2) {

			if (L[i] < R[j]) {
				arr[k] = L[i];
				i++;
			}
			else {
				arr[k] = R[j];
				j++;
			}
		}
	}
	
	
	public void mergeSort(int arr[], int l, int r) {
		int m = (l+r)/2;

		mergeSort(arr, l, m);
		mergeSort(arr, m + 1, r);

		merge(arr, l, m, r);
	}

	public static void main(String[] args) {
		int arr[] = {12, 1, 5, 3, 2, 78, 44, 32};

		MergeSort ob = new MergeSort();
		ob.mergeSort(arr, 0, arr.length);

		for (int i = 0; i < arr.length; i++)
			System.out.print(arr[i] + " ");
	}
} 
