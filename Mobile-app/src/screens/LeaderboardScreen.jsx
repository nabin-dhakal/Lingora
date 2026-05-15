import {
    View,
    Text,
    TouchableOpacity,
    FlatList,
    Dimensions,
    StyleSheet,
  } from "react-native";
import {useState} from "react";

const LeaderboardScreen = () => {
    const [leaderboardData, setLeaderboardData] = useState([
        { id: "1", name: "Alice", score: 100 },
        { id: "2", name: "Bob", score: 90 },
        { id: "3", name: "Charlie", score: 80 },
    ]);

    return (
        <View style={styles.container}>
            <Text style={styles.title}>Leaderboard</Text>
            <FlatList
                data={leaderboardData}
                keyExtractor={(item) => item.id}
                renderItem={({ item }) => (
                    <View style={styles.itemContainer}>
                        <Text style={styles.name}>{item.name}</Text>
                        <Text style={styles.score}>{item.score}</Text>
                    </View>
                )}
            />
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 20,
    },
    title: {
        fontSize: 24,
        fontWeight: "bold",
        marginBottom: 20,
    },
    itemContainer: {
        flexDirection: "row",
        justifyContent: "space-between",
        paddingVertical: 10,
        borderBottomWidth: 1,
        borderBottomColor: "#ccc",
    },
    name: {
        fontSize: 18,
    },
    score: {
        fontSize: 18,
        fontWeight: "bold",
    },
});

export default LeaderboardScreen;