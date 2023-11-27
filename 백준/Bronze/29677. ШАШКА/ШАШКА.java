import java.io.*;
import java.util.*;
import java.math.*;

public class Main {

	public static void main(String[] args) throws Throwable {
		new Main().run();
	}

	Scanner br;
	StringTokenizer st;
	boolean eof = false;

	public void run() throws Throwable {
		br = new Scanner(System.in);
		solve();
	}

	String nextToken() {
		while (st == null || !st.hasMoreTokens()) {
			try {
				st = new StringTokenizer(br.nextLine());
			} catch (Exception e) {
				eof = true;
				return "0";
			}
		}
		return st.nextToken();
	}

	int nextInt() {
		return Integer.parseInt(nextToken());
	}

	void myAssert(boolean u, String message) {
		if (!u) {
			throw new Error("Assertion failed!!! " + message);
		}
	}

	int inBounds(int x, int l, int r, String name) {
		myAssert(l <= x && x <= r, name + " not in bounds: " + x + " not in ["
				+ l + ".." + r + "]");
		return x;
	}

	String FNAME = "chess";

	private void solve() throws IOException {
		int n = inBounds(nextInt(), 2, 1000, "n");
		HashMap<String, Player> hm = new HashMap<String, Player>();
		while (n-- > 0) {
			Player p = new Player(inBounds(nextInt(), 0, 4000, "rating"),
					nextToken());
			inBounds(p.name.length(), 1, 50, "name length of " + p.name);
			hm.put(p.name, p);
		}
		int m = inBounds(nextInt(), 0, 1000, "m");
		while (m-- > 0) {
			String s1 = nextToken();
			String s2 = nextToken();
			int x = nextInt();
			myAssert(hm.containsKey(s1), "no player " + s1 + " found!!!");
			myAssert(hm.containsKey(s2), "no player " + s2 + " found!!!");
			Player p1 = hm.get(s1);
			Player p2 = hm.get(s2);
			update(p1, p2, x);
		}
		ArrayList<Player> players = new ArrayList<Player>();
		players.addAll(hm.values());
		Collections.sort(players);
		for (Player p : players) {
			System.out.println(p);
		}
	}

	private void update(Player p1, Player p2, int x) {
		double ra = p1.rating;
		double rb = p2.rating;
		double sa = x == 1 ? 1.0 : x == 0 ? 0.5 : 0.0;
		double sb = x == 2 ? 1.0 : x == 0 ? 0.5 : 0.0;
		double ea = 1.0 / (1.0 + Math.pow(10.0, (rb - ra) / 400.0));
		double eb = 1.0 / (1.0 + Math.pow(10.0, (ra - rb) / 400.0));
		p1.rating = Math.max(0, Math.round(Math.floor(ra + 15.0 * (sa - ea))));
		p2.rating = Math.max(0, Math.round(Math.floor(rb + 15.0 * (sb - eb))));
	}

	class Player implements Comparable<Player> {
		public Player(int inBounds, String nextToken) {
			rating = inBounds;
			name = nextToken;
		}

		String name;
		long rating;

		@Override
		public int compareTo(Player p) {
			if (rating == p.rating) {
				return name.compareTo(p.name);
			}
			return rating > p.rating ? -1 : 1;
		}

		@Override
		public String toString() {
			return rating + " " + name;
		}
	}

}
