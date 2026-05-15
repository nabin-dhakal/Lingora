import React from "react";
import {
  SafeAreaView,
  View,
  Text,
  StyleSheet,
  FlatList,
  TouchableOpacity,
  Dimensions,
} from "react-native";

const { width } = Dimensions.get("window");

const lessons = [
  { id: 1, completed: true, locked: false },
  { id: 2, completed: true, locked: false },
  { id: 3, completed: false, locked: false },
  { id: 4, completed: false, locked: true },
  { id: 5, completed: false, locked: true },
  { id: 6, completed: false, locked: true },
  { id: 7, completed: false, locked: true },
  { id: 8, completed: false, locked: true },
];

const getPosition = (index) => {
  const positions = [-80, 80, -60, 60, -90, 90, -50, 50];
  return positions[index % positions.length];
};

const LessonNode = ({ item, index }) => {
  const bgColor = item.locked
    ? "#d9d9d9"
    : item.completed
    ? "#58CC02"
    : "#1CB0F6";

  return (
    <View
      style={[
        styles.nodeWrapper,
        { marginLeft: width / 2 + getPosition(index) - 45 },
      ]}
    >
      <TouchableOpacity
        activeOpacity={0.8}
        style={[styles.node, { backgroundColor: bgColor }]}
      >
        <Text style={styles.nodeEmoji}>
          {item.locked ? "🔒" : item.completed ? "✓" : "⭐"}
        </Text>
      </TouchableOpacity>
    </View>
  );
};

export default function App() {
  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.header}>
        <View style={styles.headerItem}>
          <Text style={styles.headerEmoji}>🔥</Text>
          <Text style={styles.headerText}>14</Text>
        </View>

        <View style={styles.headerItem}>
          <Text style={styles.headerEmoji}>💎</Text>
          <Text style={styles.headerText}>350</Text>
        </View>

        <View style={styles.headerItem}>
          <Text style={styles.headerEmoji}>❤️</Text>
          <Text style={styles.headerText}>5</Text>
        </View>
      </View>

      <View style={styles.titleContainer}>
        <Text style={styles.title}>Sankrit Basics</Text>
        <Text style={styles.subtitle}>
          Continue your learning journey
        </Text>
      </View>

      <FlatList
        data={lessons}
        keyExtractor={(item) => item.id.toString()}
        showsVerticalScrollIndicator={false}
        contentContainerStyle={{
          paddingVertical: 40,
          paddingBottom: 120,
        }}
        renderItem={({ item, index }) => (
          <LessonNode item={item} index={index} />
        )}
      />


    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#F7F7F7",
  },

  header: {
    flexDirection: "row",
    justifyContent: "space-around",
    paddingVertical: 18,
    backgroundColor: "#fff",
    borderBottomWidth: 1,
    borderColor: "#eee",
  },

  headerItem: {
    flexDirection: "row",
    alignItems: "center",
  },

  headerEmoji: {
    fontSize: 22,
    marginRight: 6,
  },

  headerText: {
    fontSize: 18,
    fontWeight: "700",
    color: "#444",
  },

  titleContainer: {
    padding: 20,
  },

  title: {
    fontSize: 30,
    fontWeight: "800",
    color: "#333",
  },

  subtitle: {
    fontSize: 16,
    color: "#777",
    marginTop: 5,
  },

  nodeWrapper: {
    marginVertical: 18,
  },

  node: {
    width: 90,
    height: 90,
    borderRadius: 45,
    justifyContent: "center",
    alignItems: "center",

    shadowColor: "#000",
    shadowOpacity: 0.12,
    shadowRadius: 8,
    shadowOffset: {
      width: 0,
      height: 4,
    },

    elevation: 6,
  },

  nodeEmoji: {
    fontSize: 34,
    color: "#fff",
    fontWeight: "bold",
  },

  bottomBar: {
    position: "absolute",
    bottom: 20,
    left: 20,
    right: 20,
  },

  startButton: {
    backgroundColor: "#58CC02",
    paddingVertical: 18,
    borderRadius: 18,
    alignItems: "center",

    shadowColor: "#58CC02",
    shadowOpacity: 0.3,
    shadowRadius: 10,
    shadowOffset: {
      width: 0,
      height: 6,
    },

    elevation: 8,
  },

  startButtonText: {
    color: "#fff",
    fontSize: 18,
    fontWeight: "800",
    letterSpacing: 1,
  },
});